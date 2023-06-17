from rest_framework import permissions
from .models import User

class IsCourier(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == User.COURIER
        return False

class SuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == User.SUPERADMIN
        return False

class Seller(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == User.SELLER
        return False

class Assembler(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == User.ASSEMBLER
        return False

class Basic(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == User.BASIC
        return False