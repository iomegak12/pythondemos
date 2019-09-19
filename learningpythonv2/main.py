import services
import utilities

if __name__ == '__main__':
    businessProfileService = services.BusinessProfileService()
    businessProfiles = businessProfileService.getBusinessProfiles()
    table = utilities.PrettyTableGenerator.getTable(businessProfiles)

    print(table)
