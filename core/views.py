from rest_framework import generics
from rest_framework.response import Response

class WellKnownApi(generics.RetrieveAPIView):
    # {
    #     "schema_version": "v1",
    #     "name_for_human": "Blogs Plugin",
    #     "name_for_model": "Blogs",
    #     "description_for_human": "Plugin for managing a Blogs list. You can add, remove and view your Blogss.",
    #     "description_for_model": "Plugin for managing a Blogs list. You can add, remove and view your Blogss.",
    #     "auth": {
    #         "type": "none"
    #     },
    #     "api": {
    #         "type": "openapi",
    #         "url": "http://localhost:3333/openapi.yaml"
    #     },
    #     "logo_url": "http://localhost:3333/logo.png",
    #     "contact_email": "support@example.com",
    #     "legal_info_url": "http://www.example.com/legal"
    # }
    def get(self, request, *args, **kwargs):
        return Response({
            "schema_version": "v1",
            "name_for_human": "Blogs Plugin",
            "name_for_model": "Blogs",
            "description_for_human": "Plugin for managing a Blogs list. You can add, remove and view your Blogs.",
            "description_for_model": "Plugin for managing a Blogs list. You can add, remove and view your Blogs.",
            "auth": {
                "type": "none"
            },
            "api": {
                "type": "openapi",
                "url": "http://localhost:8000/api/schema"
            },
            "logo_url": "http://localhost:8000/images/logo.png",
            "contact_email": "contact.shihab.247@gmail.com",
            "legal_info_url": "http://localhost:8000/legal"
        })