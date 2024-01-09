from rest_framework import permissions


class IsManagementUser(permissions.BasePermission):
    # A custom permission class that only allows management users to access the view

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the management role
        return request.user.is_authenticated and request.user.role == 1


class IsSales_ManagerUser(permissions.BasePermission):
    # A custom permission class that only allows sales_manager users to access the view

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the sales_manager role
        return request.user.is_authenticated and request.user.role == 2


class IsSupporterUser(permissions.BasePermission):
    # A custom permission class that only allows supporter users to access the view

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the supporter role
        return request.user.is_authenticated and request.user.role == 3


class IsConsultantUser(permissions.BasePermission):
    # A custom permission class that only allows consultant users to access the view

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the consultant role
        return request.user.is_authenticated and request.user.role == 4


class IsAccountingUser(permissions.BasePermission):
    # A custom permission class that only allows accounting users to access the view

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the accounting role
        return request.user.is_authenticated and request.user.role == 5


class IsMEDREP_VisitorUser(permissions.BasePermission):
    # A custom permission class that only allows medrep_visitor users to access the view

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the medrep_visitor role
        return request.user.is_authenticated and request.user.role == 6


class IsVisitorUser(permissions.BasePermission):
    # A custom permission class that only allows visitor users to access the view

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the visitor role
        return request.user.is_authenticated and request.user.role == 7
