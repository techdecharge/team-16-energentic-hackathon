
from fastapi import APIRouter

from app.beckenServices.confirm import confirm_selection
from app.beckenServices.order_status import fetch_order_details
from app.beckenServices.search import send_search_request
from app.worldEngineSerives.utility_details import fetch_company_details

router = APIRouter()


@router.get("/program/search")
def list_programs():
    result = send_search_request()
    return result


@router.get("/program/confirm/{provider_id}/{item_id}")
async def program_confirmation(provider_id, item_id):
    print(provider_id)
    print(item_id)
    result = confirm_selection(provider_id, item_id)
    return result


@router.get("/order/status/{order_id}")
async def order_status(order_id):
    print(order_id)
    result = fetch_order_details(order_id)
    return result


@router.get("/company/details/{company_name}")
async def company_details(company_name):
    print(company_name)
    result = fetch_company_details(company_name)
    return result
