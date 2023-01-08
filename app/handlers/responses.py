import json
from typing import Dict

from flask import Response


class ApiResponse:
    __DEFAULT_MIMETYPE = 'application/json'

    @staticmethod
    def response200(data: Dict,
                    mimetype: str = __DEFAULT_MIMETYPE) -> Response:
        # Todo specify data type by using generic types

        response_data = json.dumps(data)

        return Response(
            headers={'Access-Control-Allow-Origin': '*'},
            response=response_data,
            mimetype=mimetype,
            status=200
        )

    # Todo: 5.., 4.. and other responses
