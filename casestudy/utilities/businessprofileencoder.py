import models

INVALID_ARGUMENTS = 'Invalid Argument Specified!'


class BusinessProfileEncoder:
    def transform(dictionary):
        if dictionary is None:
            raise Exception(INVALID_ARGUMENTS)

        businessProfile = models.CustomerProfile(
            dictionary['id'], dictionary['fullName'],
            dictionary['avatar'], dictionary['city'], dictionary['email'],
            dictionary['phone'])

        return businessProfile
