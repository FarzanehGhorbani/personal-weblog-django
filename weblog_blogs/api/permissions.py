from rest_framework.permissions import BasePermission,SAFE_METHODS

class OwnerCanManagerOrReadOnly(BasePermission):
    message=''

    def has_permission(self, request, view):  #view level
        self.message='Your request does not have permission or you are is not'
        if request.method in SAFE_METHODS:
            return True
        elif not request.user.is_anonymous:
            return True
        else:
            return False


    def has_object_permission(self, request, view, obj): #object level
        self.message='You must be the owner of this object'
        return request.user == obj.owner
