from django.shortcuts import redirect


class CheckForRestriction:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('home')

        data = super().dispatch(request, *args, **kwargs)
        return data
