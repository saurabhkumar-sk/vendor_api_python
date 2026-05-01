from fastapi import FastAPI
from app.apis.v1.endpoints import vendor
from app.core.exception_handler import validation_exception_handler
from fastapi.exceptions import RequestValidationError


app = FastAPI()

app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(
    vendor.router,
    prefix= "/api/v1/vendors",
    tags=["Vendors"]
)
