from fastapi import FastAPI
from ucars.routers.v1.router_v1 import router_v1
from ucars.routers.v2.router_v2 import router_v2


app = FastAPI(
    title="UCars API",
    description="Cars Management System",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Github",
        "url": "https://github.com/quan-vu/UCars",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)


# Register APIs
app.include_router(router_v1)
app.include_router(router_v2)

