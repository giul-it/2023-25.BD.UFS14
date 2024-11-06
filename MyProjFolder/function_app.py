import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

from mongo_database import sperofunzioni



@app.route(route="MyHttpTrigger", auth_level=func.AuthLevel.ANONYMOUS)
def MyHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    num = req.params.get(num)
    if not num:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get(num)

    if num:
        return func.HttpResponse(f"{sperofunzioni(num)}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )