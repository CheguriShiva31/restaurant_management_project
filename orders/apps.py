from django.http import JsonResponse
from.models import MenuItem
def menu_item_view(request):
    try:
        list(MenuItem.objects.values("id","name","price"))
        return JsonResponse({"menu_items": items},status=200)
        except MenuItem.DoesNotExists:
            return JsonResponse({"error:"No menu items found"}, status=404)
            except Exception as e:
                return JsonResponse({"error":f"something went wrong: {str(e)}"}, status=500)