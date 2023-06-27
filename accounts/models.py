from django.contrib.auth import models as auth_models

from farm import models as farm_models

class User(auth_models.User):
    def save(self, *args, **kwargs):
        if self._state.adding:
            user = super().save(*args, **kwargs)
            farmer = farm_models.Farmer(
                first_name=self.first_name,
                surname=self.last_name,
                user=self
            )
            farmer.save()
            return user
        else:
            return super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.username} ({self.email})"
