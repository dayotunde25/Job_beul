import requests

url = "https://active-jobs-db.p.rapidapi.com/active-ats-24h"

querystring = {"title_filter":"","description_type":"text"}

headers = {
	"x-rapidapi-key": "b85e43b376msh24baf6ffbcfeeb3p14438ajsn3a55fc11c03d",
	"x-rapidapi-host": "active-jobs-db.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())


[
  {
    "id": "1862266284",
    "date_posted": "2025-09-02T14:36:37",
    "date_created": "2025-09-02T09:57:41.134402",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "5390 Great America Parkway",
          "addressLocality": "Santa Clara",
          "addressRegion": "CA",
          "postalCode": "95054",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 18.2,
        "maxValue": 20.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541131",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Santa Clara"
    ],
    "counties_derived": [
      "Santa Clara County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Santa Clara, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.40804139438906
    ],
    "lngs_derived": [
      -121.97789166295381
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266152",
    "date_posted": "2025-09-02T14:33:17",
    "date_created": "2025-09-02T09:56:12.012082",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "5390 Great America Parkway",
          "addressLocality": "Santa Clara",
          "addressRegion": "CA",
          "postalCode": "95054",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17.2,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541130",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Santa Clara"
    ],
    "counties_derived": [
      "Santa Clara County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Santa Clara, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.40804139438906
    ],
    "lngs_derived": [
      -121.97789166295381
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266151",
    "date_posted": "2025-09-02T14:25:51",
    "date_created": "2025-09-02T09:56:11.712838",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "6031 Lone Tree Way",
          "addressLocality": "Brentwood",
          "addressRegion": "CA",
          "postalCode": "94513",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541128",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Brentwood"
    ],
    "counties_derived": [
      "Contra Costa County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Brentwood, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.961556
    ],
    "lngs_derived": [
      -121.7409346
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266154",
    "date_posted": "2025-09-02T14:24:35",
    "date_created": "2025-09-02T09:56:12.180169",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "6031 Lone Tree Way",
          "addressLocality": "Brentwood",
          "addressRegion": "CA",
          "postalCode": "94513",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 18,
        "maxValue": 21,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541127",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Brentwood"
    ],
    "counties_derived": [
      "Contra Costa County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Brentwood, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.961556
    ],
    "lngs_derived": [
      -121.7409346
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266155",
    "date_posted": "2025-09-02T14:22:53",
    "date_created": "2025-09-02T09:56:12.297047",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1944 Anderson Road",
          "addressLocality": "Davis",
          "addressRegion": "CA",
          "postalCode": "95616",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541126",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Davis"
    ],
    "counties_derived": [
      "Yolo County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Davis, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.560281
    ],
    "lngs_derived": [
      -121.758387
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266150",
    "date_posted": "2025-09-02T14:21:36",
    "date_created": "2025-09-02T09:56:09.153946",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1944 Anderson Road",
          "addressLocality": "Davis",
          "addressRegion": "CA",
          "postalCode": "95616",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541123",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Davis"
    ],
    "counties_derived": [
      "Yolo County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Davis, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.560281
    ],
    "lngs_derived": [
      -121.758387
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266230",
    "date_posted": "2025-09-02T14:16:15",
    "date_created": "2025-09-02T09:57:07.617841",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "7969 Watt Ave.",
          "addressLocality": "Antelope",
          "addressRegion": "CA",
          "postalCode": "95843",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541122",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Antelope"
    ],
    "counties_derived": [
      "Sacramento County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Antelope, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.71368595356825
    ],
    "lngs_derived": [
      -121.39237105017656
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266174",
    "date_posted": "2025-09-02T14:09:30",
    "date_created": "2025-09-02T09:56:19.473141",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "7969 Watt Ave.",
          "addressLocality": "Antelope",
          "addressRegion": "CA",
          "postalCode": "95843",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541121",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Antelope"
    ],
    "counties_derived": [
      "Sacramento County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Antelope, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.71368595356825
    ],
    "lngs_derived": [
      -121.39237105017656
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266172",
    "date_posted": "2025-09-02T14:03:07",
    "date_created": "2025-09-02T09:56:17.557584",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "4050 Florin Road",
          "addressLocality": "Sacramento",
          "addressRegion": "CA",
          "postalCode": "95823",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541119",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Sacramento"
    ],
    "counties_derived": [
      "Sacramento County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Sacramento, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.49592554198082
    ],
    "lngs_derived": [
      -121.45989106757982
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266166",
    "date_posted": "2025-09-02T14:02:07",
    "date_created": "2025-09-02T09:56:13.142438",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "4050 Florin Road",
          "addressLocality": "Sacramento",
          "addressRegion": "CA",
          "postalCode": "95823",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541118",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Sacramento"
    ],
    "counties_derived": [
      "Sacramento County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Sacramento, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.49592554198082
    ],
    "lngs_derived": [
      -121.45989106757982
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266226",
    "date_posted": "2025-09-02T14:00:21",
    "date_created": "2025-09-02T09:57:05.085751",
    "title": "Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "42197 Margarita Rd.",
          "addressLocality": "Temecula",
          "addressRegion": "CA",
          "postalCode": "92591",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 21,
        "maxValue": 23,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541117",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Temecula"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Temecula, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.511008408797004
    ],
    "lngs_derived": [
      -117.12378835193624
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position calls for people who are adept at both assisting customers and leading a diverse team of individuals. In the role of Team Leader, you'll be responsible for managing all aspects of the store's operation—a responsibility you'll prepare for through a training sequence that teaches you the company in-store retail information system, inventory management and ordering technology.\nYou will be tasked with handling daily paperwork, troubleshooting car wash issues and other gas pump related issues. This leadership role will also include forecasting, ordering, stocking, and merchandising products, reconciling store paperwork, setting the tone for courteous customer service, and managing the store staff.\nWe expect all of our Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTrain and coach new staff, manage performance, and handle staffing needs\nCreate schedules, track time, and ensure accurate store paperwork reconciliation\nStock products, maintain store cleanliness, and manage product merchandising\nForecast, order, and control inventory, with a focus on shrinkage control\nTrack and manage operating expenses to ensure profitability\nDevelop a sales-driven culture using data analysis, goal setting, and in-store operating profit management\nEnsure efficient, courteous customer service for customers, vendors, and staff\nTroubleshoot and resolve car wash and gas-related issues\nMaintain compliance with local, state, and federal regulations and budget requirements\nMaintain a clean, customer-friendly environment inside and outside the store\nPerform additional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager, manager, or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nValid driver’s license and insurance\nReliable form of transportation to and from the workplace and off-site training\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Team Leader position requires constant standing, bending and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Requirements:\nMust be 21+ years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$21.00 - $25.00/per hour"
  },
  {
    "id": "1862266169",
    "date_posted": "2025-09-02T13:53:27",
    "date_created": "2025-09-02T09:56:15.574805",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "42197 Margarita Rd.",
          "addressLocality": "Temecula",
          "addressRegion": "CA",
          "postalCode": "92591",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541115",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Temecula"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Temecula, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.511008408797004
    ],
    "lngs_derived": [
      -117.12378835193624
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266212",
    "date_posted": "2025-09-02T13:51:47",
    "date_created": "2025-09-02T09:57:03.069369",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "26721 Rancho Pkwy",
          "addressLocality": "Lake Forrest",
          "addressRegion": "CA",
          "postalCode": "92630",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541114",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Lake Forest"
    ],
    "counties_derived": [
      "Orange County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Lake Forest, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.641467348747966
    ],
    "lngs_derived": [
      -117.68944770964356
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266218",
    "date_posted": "2025-09-02T13:50:43",
    "date_created": "2025-09-02T09:57:04.596623",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "26721 Rancho Pkwy",
          "addressLocality": "Lake Forrest",
          "addressRegion": "CA",
          "postalCode": "92630",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 18.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541113",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Lake Forest"
    ],
    "counties_derived": [
      "Orange County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Lake Forest, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.641467348747966
    ],
    "lngs_derived": [
      -117.68944770964356
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266191",
    "date_posted": "2025-09-02T13:47:17",
    "date_created": "2025-09-02T09:56:44.346979",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "2085 Novato Blvd.",
          "addressLocality": "Novato",
          "addressRegion": "CA",
          "postalCode": "94947",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17.27,
        "maxValue": 19.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541112",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Novato"
    ],
    "counties_derived": [
      "Marin County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Novato, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.1117494
    ],
    "lngs_derived": [
      -122.593423
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266153",
    "date_posted": "2025-09-02T13:45:05",
    "date_created": "2025-09-02T09:56:12.035283",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "2085 Novato Blvd.",
          "addressLocality": "Novato",
          "addressRegion": "CA",
          "postalCode": "94947",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 22,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541111",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Novato"
    ],
    "counties_derived": [
      "Marin County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Novato, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.1117494
    ],
    "lngs_derived": [
      -122.593423
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\n\nAbout the Company\n\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266168",
    "date_posted": "2025-09-02T13:40:34",
    "date_created": "2025-09-02T09:56:15.51225",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "950 Del Presidio Blvd.",
          "addressLocality": "San Rafael",
          "addressRegion": "CA",
          "postalCode": "94901",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541110",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "San Rafael"
    ],
    "counties_derived": [
      "Marin County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "San Rafael, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.00686668841044
    ],
    "lngs_derived": [
      -122.54424873901942
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\n\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266175",
    "date_posted": "2025-09-02T13:38:55",
    "date_created": "2025-09-02T09:56:19.962093",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "950 Del Presidio Blvd.",
          "addressLocality": "San Rafael",
          "addressRegion": "CA",
          "postalCode": "94901",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 22,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541109",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "San Rafael"
    ],
    "counties_derived": [
      "Marin County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "San Rafael, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.00686668841044
    ],
    "lngs_derived": [
      -122.54424873901942
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266200",
    "date_posted": "2025-09-02T13:33:00",
    "date_created": "2025-09-02T09:56:47.711149",
    "title": "Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "106 S Sanderson Ave.",
          "addressLocality": "San Jacinto",
          "addressRegion": "CA",
          "postalCode": "92571",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 21,
        "maxValue": 23,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541108",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Perris"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Perris, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.80735889047619
    ],
    "lngs_derived": [
      -117.2197217984127
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Leader\n\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position calls for people who are adept at both assisting customers and leading a diverse team of individuals. In the role of Team Leader, you'll be responsible for managing all aspects of the store's operation—a responsibility you'll prepare for through a training sequence that teaches you the company in-store retail information system, inventory management and ordering technology.\nYou will be tasked with handling daily paperwork, troubleshooting car wash issues and other gas pump related issues. This leadership role will also include forecasting, ordering, stocking, and merchandising products, reconciling store paperwork, setting the tone for courteous customer service, and managing the store staff.\nWe expect all of our Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTrain and coach new staff, manage performance, and handle staffing needs\nCreate schedules, track time, and ensure accurate store paperwork reconciliation\nStock products, maintain store cleanliness, and manage product merchandising\nForecast, order, and control inventory, with a focus on shrinkage control\nTrack and manage operating expenses to ensure profitability\nDevelop a sales-driven culture using data analysis, goal setting, and in-store operating profit management\nEnsure efficient, courteous customer service for customers, vendors, and staff\nTroubleshoot and resolve car wash and gas-related issues\nMaintain compliance with local, state, and federal regulations and budget requirements\nMaintain a clean, customer-friendly environment inside and outside the store\nPerform additional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager, manager, or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nValid driver’s license and insurance\nReliable form of transportation to and from the workplace and off-site training\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Team Leader position requires constant standing, bending and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Requirements:\nMust be 21+ years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$21.00 - $25.00/per hour"
  },
  {
    "id": "1862266165",
    "date_posted": "2025-09-02T13:32:17",
    "date_created": "2025-09-02T09:56:12.726842",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "106 S Sanderson Ave.",
          "addressLocality": "San Jacinto",
          "addressRegion": "CA",
          "postalCode": "92571",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 18.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541107",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Perris"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Perris, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.80735889047619
    ],
    "lngs_derived": [
      -117.2197217984127
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266177",
    "date_posted": "2025-09-02T13:30:49",
    "date_created": "2025-09-02T09:56:20.025513",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "106 S Sanderson Ave.",
          "addressLocality": "San Jacinto",
          "addressRegion": "CA",
          "postalCode": "92571",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541106",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Perris"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Perris, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.80735889047619
    ],
    "lngs_derived": [
      -117.2197217984127
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266190",
    "date_posted": "2025-09-02T13:28:16",
    "date_created": "2025-09-02T09:56:40.695357",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1698 Tully Road",
          "addressLocality": "San Jose",
          "addressRegion": "CA",
          "postalCode": "95122",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17.95,
        "maxValue": 20.45,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541105",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "San Jose"
    ],
    "counties_derived": [
      "Santa Clara County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "San Jose, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.32826432116105
    ],
    "lngs_derived": [
      -121.83574986218164
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266217",
    "date_posted": "2025-09-02T13:26:25",
    "date_created": "2025-09-02T09:57:04.339602",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1698 Tully Road",
          "addressLocality": "San Jose",
          "addressRegion": "CA",
          "postalCode": "95122",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541104",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "San Jose"
    ],
    "counties_derived": [
      "Santa Clara County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "San Jose, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.32826432116105
    ],
    "lngs_derived": [
      -121.83574986218164
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266211",
    "date_posted": "2025-09-02T13:21:20",
    "date_created": "2025-09-02T09:57:02.570018",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "834 Irwin St.",
          "addressLocality": "San Rafael",
          "addressRegion": "CA",
          "postalCode": "94901",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541102",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "San Rafael"
    ],
    "counties_derived": [
      "Marin County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "San Rafael, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.97074873655532
    ],
    "lngs_derived": [
      -122.520977857765
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266214",
    "date_posted": "2025-09-02T13:20:07",
    "date_created": "2025-09-02T09:57:03.600805",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "834 Irwin St.",
          "addressLocality": "San Rafael",
          "addressRegion": "CA",
          "postalCode": "94901",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 22,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541100",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "San Rafael"
    ],
    "counties_derived": [
      "Marin County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "San Rafael, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.97074873655532
    ],
    "lngs_derived": [
      -122.520977857765
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266216",
    "date_posted": "2025-09-02T13:18:01",
    "date_created": "2025-09-02T09:57:04.215524",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1610 Meridian Avenue",
          "addressLocality": "San Jose",
          "addressRegion": "CA",
          "postalCode": "95125",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17.95,
        "maxValue": 20.45,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541098",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "San Jose"
    ],
    "counties_derived": [
      "Santa Clara County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "San Jose, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.295056
    ],
    "lngs_derived": [
      -121.89144
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266210",
    "date_posted": "2025-09-02T13:09:52",
    "date_created": "2025-09-02T09:57:01.842425",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1610 Meridian Avenue",
          "addressLocality": "San Jose",
          "addressRegion": "CA",
          "postalCode": "95125",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541096",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "San Jose"
    ],
    "counties_derived": [
      "Santa Clara County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "San Jose, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.295056
    ],
    "lngs_derived": [
      -121.89144
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266213",
    "date_posted": "2025-09-02T13:07:09",
    "date_created": "2025-09-02T09:57:03.48611",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "708 Admiral Callaghan Lane",
          "addressLocality": "Vallejo",
          "addressRegion": "CA",
          "postalCode": "94590",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541095",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Vallejo"
    ],
    "counties_derived": [
      "Solano County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Vallejo, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.123766530612244
    ],
    "lngs_derived": [
      -122.22780553061224
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266167",
    "date_posted": "2025-09-02T13:04:50",
    "date_created": "2025-09-02T09:56:14.147025",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "708 Admiral Callaghan Lane",
          "addressLocality": "Vallejo",
          "addressRegion": "CA",
          "postalCode": "94590",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 18,
        "maxValue": 21,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541094",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Vallejo"
    ],
    "counties_derived": [
      "Solano County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Vallejo, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.123766530612244
    ],
    "lngs_derived": [
      -122.22780553061224
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\n\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266171",
    "date_posted": "2025-09-02T13:01:17",
    "date_created": "2025-09-02T09:56:17.497256",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "25361 Railroad Canyon Road",
          "addressLocality": "Lake Elsinore",
          "addressRegion": "CA",
          "postalCode": "92532",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 18.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541093",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Lake Elsinore"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Lake Elsinore, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.66816596322009
    ],
    "lngs_derived": [
      -117.26408948232265
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266176",
    "date_posted": "2025-09-02T12:58:53",
    "date_created": "2025-09-02T09:56:19.98514",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "25361 Railroad Canyon Road",
          "addressLocality": "Lake Elsinore",
          "addressRegion": "CA",
          "postalCode": "92532",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541092",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Lake Elsinore"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Lake Elsinore, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.66816596322009
    ],
    "lngs_derived": [
      -117.26408948232265
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266215",
    "date_posted": "2025-09-02T12:52:30",
    "date_created": "2025-09-02T09:57:03.804983",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "8607 Elk Grove Blvd.",
          "addressLocality": "Elk Grove",
          "addressRegion": "CA",
          "postalCode": "95624",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541091",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Elk Grove"
    ],
    "counties_derived": [
      "Sacramento County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Elk Grove, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.4094459
    ],
    "lngs_derived": [
      -121.385058
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266178",
    "date_posted": "2025-09-02T12:51:07",
    "date_created": "2025-09-02T09:56:20.393591",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "8607 Elk Grove Blvd.",
          "addressLocality": "Elk Grove",
          "addressRegion": "CA",
          "postalCode": "95624",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541090",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Elk Grove"
    ],
    "counties_derived": [
      "Sacramento County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Elk Grove, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.4094459
    ],
    "lngs_derived": [
      -121.385058
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266173",
    "date_posted": "2025-09-02T12:47:06",
    "date_created": "2025-09-02T09:56:19.28089",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1235 California Avenue",
          "addressLocality": "Pittsburg",
          "addressRegion": "CA",
          "postalCode": "94565",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541089",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Pittsburg"
    ],
    "counties_derived": [
      "Contra Costa County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Pittsburg, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.01303731521878
    ],
    "lngs_derived": [
      -121.8676554857444
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266180",
    "date_posted": "2025-09-02T12:45:50",
    "date_created": "2025-09-02T09:56:22.142885",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1235 California Avenue",
          "addressLocality": "Pittsburg",
          "addressRegion": "CA",
          "postalCode": "94565",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 18,
        "maxValue": 21,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541088",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Pittsburg"
    ],
    "counties_derived": [
      "Contra Costa County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Pittsburg, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.01303731521878
    ],
    "lngs_derived": [
      -121.8676554857444
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266179",
    "date_posted": "2025-09-02T12:44:22",
    "date_created": "2025-09-02T09:56:21.086879",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "7300 Redwood Blvd.",
          "addressLocality": "Novato",
          "addressRegion": "CA",
          "postalCode": "94947",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 22,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541087",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Novato"
    ],
    "counties_derived": [
      "Marin County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Novato, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.105069
    ],
    "lngs_derived": [
      -122.570729
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862266207",
    "date_posted": "2025-09-02T12:43:11",
    "date_created": "2025-09-02T09:56:51.398647",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "7300 Redwood Blvd.",
          "addressLocality": "Novato",
          "addressRegion": "CA",
          "postalCode": "94947",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17.27,
        "maxValue": 19.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541085",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Novato"
    ],
    "counties_derived": [
      "Marin County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Novato, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.105069
    ],
    "lngs_derived": [
      -122.570729
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266149",
    "date_posted": "2025-09-02T12:41:27",
    "date_created": "2025-09-02T09:55:58.75021",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "3490 Marron Road",
          "addressLocality": "Oceanside",
          "addressRegion": "CA",
          "postalCode": "92054",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 18.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541082",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Oceanside"
    ],
    "counties_derived": [
      "San Diego County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Oceanside, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.178561253761615
    ],
    "lngs_derived": [
      -117.29452208344887
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862266170",
    "date_posted": "2025-09-02T12:40:09",
    "date_created": "2025-09-02T09:56:15.717872",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "3490 Marron Road",
          "addressLocality": "Oceanside",
          "addressRegion": "CA",
          "postalCode": "92054",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541080",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Oceanside"
    ],
    "counties_derived": [
      "San Diego County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Oceanside, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.178561253761615
    ],
    "lngs_derived": [
      -117.29452208344887
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223593",
    "date_posted": "2025-09-02T12:38:32",
    "date_created": "2025-09-02T07:59:36.933171",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "2800 Augustine Drive",
          "addressLocality": "Santa Clara",
          "addressRegion": "CA",
          "postalCode": "95054",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 18.2,
        "maxValue": 20.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541079",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Santa Clara"
    ],
    "counties_derived": [
      "Santa Clara County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Santa Clara, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.382243
    ],
    "lngs_derived": [
      -121.978342
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862223604",
    "date_posted": "2025-09-02T12:37:34",
    "date_created": "2025-09-02T07:59:46.907099",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "2800 Augustine Drive",
          "addressLocality": "Santa Clara",
          "addressRegion": "CA",
          "postalCode": "95054",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17.2,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541076",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Santa Clara"
    ],
    "counties_derived": [
      "Santa Clara County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Santa Clara, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.382243
    ],
    "lngs_derived": [
      -121.978342
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\n\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223607",
    "date_posted": "2025-09-02T12:34:02",
    "date_created": "2025-09-02T07:59:53.555836",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "500 E San Jacinto Ave.",
          "addressLocality": "Perris",
          "addressRegion": "CA",
          "postalCode": "92571",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 18.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541075",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Perris"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Perris, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.786677
    ],
    "lngs_derived": [
      -117.215155
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862223594",
    "date_posted": "2025-09-02T12:32:57",
    "date_created": "2025-09-02T07:59:37.120849",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "500 E San Jacinto Ave.",
          "addressLocality": "Perris",
          "addressRegion": "CA",
          "postalCode": "92571",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541074",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Perris"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Perris, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.786677
    ],
    "lngs_derived": [
      -117.215155
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223602",
    "date_posted": "2025-09-02T12:31:29",
    "date_created": "2025-09-02T07:59:38.77338",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "790 E El Camino Real",
          "addressLocality": "Mountain View",
          "addressRegion": "CA",
          "postalCode": "94040",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17.95,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541072",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Mountain View"
    ],
    "counties_derived": [
      "Santa Clara County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Mountain View, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.37659387473915
    ],
    "lngs_derived": [
      -122.06386899204288
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223600",
    "date_posted": "2025-09-02T12:29:14",
    "date_created": "2025-09-02T07:59:38.386306",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "790 E El Camino Real",
          "addressLocality": "Mountain View",
          "addressRegion": "CA",
          "postalCode": "94040",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 19.2,
        "maxValue": 21.3,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541071",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Mountain View"
    ],
    "counties_derived": [
      "Santa Clara County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Mountain View, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.37659387473915
    ],
    "lngs_derived": [
      -122.06386899204288
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862223590",
    "date_posted": "2025-09-02T12:27:31",
    "date_created": "2025-09-02T07:59:36.378253",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "7401 Sheldon Rd.",
          "addressLocality": "Elk Grove",
          "addressRegion": "CA",
          "postalCode": "95758",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 18.5,
        "maxValue": 20.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541070",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Elk Grove"
    ],
    "counties_derived": [
      "Sacramento County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Elk Grove, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.438494
    ],
    "lngs_derived": [
      -121.416964
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223595",
    "date_posted": "2025-09-02T12:25:13",
    "date_created": "2025-09-02T07:59:37.380138",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "7401 Sheldon Rd.",
          "addressLocality": "Elk Grove",
          "addressRegion": "CA",
          "postalCode": "95758",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541069",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Elk Grove"
    ],
    "counties_derived": [
      "Sacramento County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Elk Grove, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.438494
    ],
    "lngs_derived": [
      -121.416964
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862223588",
    "date_posted": "2025-09-02T12:21:10",
    "date_created": "2025-09-02T07:59:35.779946",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "26680 Ynez Rd.",
          "addressLocality": "Temecula",
          "addressRegion": "CA",
          "postalCode": "92591",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 18.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541068",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Temecula"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Temecula, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.515281673750124
    ],
    "lngs_derived": [
      -117.15530753048513
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862223599",
    "date_posted": "2025-09-02T12:19:58",
    "date_created": "2025-09-02T07:59:38.188596",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "26680 Ynez Rd.",
          "addressLocality": "Temecula",
          "addressRegion": "CA",
          "postalCode": "92591",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541067",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Temecula"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Temecula, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.515281673750124
    ],
    "lngs_derived": [
      -117.15530753048513
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223601",
    "date_posted": "2025-09-02T12:18:27",
    "date_created": "2025-09-02T07:59:38.531008",
    "title": "Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "26680 Ynez Rd.",
          "addressLocality": "Temecula",
          "addressRegion": "CA",
          "postalCode": "92591",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 21,
        "maxValue": 23,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541066",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Temecula"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Temecula, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.515281673750124
    ],
    "lngs_derived": [
      -117.15530753048513
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\n\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience. Our mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team. Apply today and help us change the way people experience convenience!\n\nPosition Summary:\nThis position calls for people who are adept at both assisting customers and leading a diverse team of individuals. In the role of Team Leader, you'll be responsible for managing all aspects of the store's operation—a responsibility you'll prepare for through a training sequence that teaches you the company in-store retail information system, inventory management and ordering technology.\n\nYou will be tasked with handling daily paperwork, troubleshooting car wash issues and other gas pump related issues. This leadership role will also include forecasting, ordering, stocking, and merchandising products, reconciling store paperwork, setting the tone for courteous customer service, and managing the store staff.\n\nWe expect all our Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles. Below is a general outline of some of the roles and responsibilities expected of our Team Leaders (this list is not all inclusive):\n\nPrimary Responsibilities:\nTrain and coach new staff, manage performance, and handle staffing needs\nCreate schedules, track time, and ensure accurate store paperwork reconciliation\nStock products, maintain store cleanliness, and manage product merchandising\nForecast, order, and control inventory, with a focus on shrinkage control\nTrack and manage operating expenses to ensure profitability\nDevelop a sales-driven culture using data analysis, goal setting, and in-store operating profit management\nEnsure efficient, courteous customer service for customers, vendors, and staff\nTroubleshoot and resolve car wash and gas-related issues\nMaintain compliance with local, state, and federal regulations and budget requirements\nMaintain a clean, customer-friendly environment inside and outside the store\nPerform additional duties as assigned\nRequirements\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager, manager, or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nValid driver’s license and insurance\nReliable form of transportation to and from the workplace and off-site training\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that have been with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Team Leader position requires constant standing, bending and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Requirements:\nMust be 21+ years of age\nMust be able to work various shifts and days of the week depending on business needs"
  },
  {
    "id": "1862223605",
    "date_posted": "2025-09-02T12:15:59",
    "date_created": "2025-09-02T07:59:47.583519",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "6490 Mack Road",
          "addressLocality": "Sacramento",
          "addressRegion": "CA",
          "postalCode": "95828",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541065",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Sacramento"
    ],
    "counties_derived": [
      "Sacramento County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Sacramento, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.47413536180904
    ],
    "lngs_derived": [
      -121.42742143718593
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223589",
    "date_posted": "2025-09-02T12:14:20",
    "date_created": "2025-09-02T07:59:36.169826",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "15236 US HWY 395",
          "addressLocality": "ADELANTO",
          "addressRegion": "CA",
          "postalCode": "92301",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541064",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Adelanto"
    ],
    "counties_derived": [
      "San Bernardino County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Adelanto, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      34.514554
    ],
    "lngs_derived": [
      -117.403913
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223587",
    "date_posted": "2025-09-02T12:13:34",
    "date_created": "2025-09-02T07:59:35.585126",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "15236 US HWY 395",
          "addressLocality": "ADELANTO",
          "addressRegion": "CA",
          "postalCode": "92301",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "unitText": "HOUR",
        "value": 16.5
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541063",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Adelanto"
    ],
    "counties_derived": [
      "San Bernardino County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Adelanto, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      34.514554
    ],
    "lngs_derived": [
      -117.403913
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862223592",
    "date_posted": "2025-09-02T12:12:34",
    "date_created": "2025-09-02T07:59:36.757125",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1833 4th St.",
          "addressLocality": "San Rafael",
          "addressRegion": "CA",
          "postalCode": "94901",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 22,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541062",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "San Rafael"
    ],
    "counties_derived": [
      "Marin County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "San Rafael, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.9741515784063
    ],
    "lngs_derived": [
      -122.54003058069874
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\n\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223598",
    "date_posted": "2025-09-02T12:11:27",
    "date_created": "2025-09-02T07:59:38.010694",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1833 4th St.",
          "addressLocality": "San Rafael",
          "addressRegion": "CA",
          "postalCode": "94901",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541061",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "San Rafael"
    ],
    "counties_derived": [
      "Marin County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "San Rafael, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.9741515784063
    ],
    "lngs_derived": [
      -122.54003058069874
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862223591",
    "date_posted": "2025-09-02T12:09:49",
    "date_created": "2025-09-02T07:59:36.580469",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1728 Oakdale Rd.",
          "addressLocality": "Modesto",
          "addressRegion": "CA",
          "postalCode": "95355",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 19,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541060",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Modesto"
    ],
    "counties_derived": [
      "Stanislaus County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Modesto, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.66918975
    ],
    "lngs_derived": [
      -120.95719142421939
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862223596",
    "date_posted": "2025-09-02T12:08:58",
    "date_created": "2025-09-02T07:59:37.6717",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "1728 Oakdale Rd.",
          "addressLocality": "Modesto",
          "addressRegion": "CA",
          "postalCode": "95355",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541059",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Modesto"
    ],
    "counties_derived": [
      "Stanislaus County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Modesto, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.66918975
    ],
    "lngs_derived": [
      -120.95719142421939
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223603",
    "date_posted": "2025-09-02T12:04:57",
    "date_created": "2025-09-02T07:59:38.989379",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "29971 Antelope Rd.",
          "addressLocality": "Menifee",
          "addressRegion": "CA",
          "postalCode": "92584",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 16.5,
        "maxValue": 18.5,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541058",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Menifee"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Menifee, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.68734683939257
    ],
    "lngs_derived": [
      -117.16939672272935
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862223597",
    "date_posted": "2025-09-02T12:01:35",
    "date_created": "2025-09-02T07:59:37.818773",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "29971 Antelope Rd.",
          "addressLocality": "Menifee",
          "addressRegion": "CA",
          "postalCode": "92584",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 20,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541057",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Menifee"
    ],
    "counties_derived": [
      "Riverside County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Menifee, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      33.68734683939257
    ],
    "lngs_derived": [
      -117.16939672272935
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223661",
    "date_posted": "2025-09-02T11:58:19",
    "date_created": "2025-09-02T08:01:01.840277",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "777 Steele Lane",
          "addressLocality": "Santa Rosa",
          "addressRegion": "CA",
          "postalCode": "95403",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17.87,
        "maxValue": 20.2,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541056",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Santa Rosa"
    ],
    "counties_derived": [
      "Sonoma County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Santa Rosa, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.4603672
    ],
    "lngs_derived": [
      -122.7252581
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862223606",
    "date_posted": "2025-09-02T11:57:07",
    "date_created": "2025-09-02T07:59:49.350415",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "777 Steele Lane",
          "addressLocality": "Santa Rosa",
          "addressRegion": "CA",
          "postalCode": "95403",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17.06,
        "maxValue": 21,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541055",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Santa Rosa"
    ],
    "counties_derived": [
      "Sonoma County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Santa Rosa, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.4603672
    ],
    "lngs_derived": [
      -122.7252581
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223608",
    "date_posted": "2025-09-02T11:54:58",
    "date_created": "2025-09-02T07:59:54.713705",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "6301 Hembree Lane",
          "addressLocality": "Windsor",
          "addressRegion": "CA",
          "postalCode": "95492",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17.06,
        "maxValue": 20.2,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541053",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Windsor"
    ],
    "counties_derived": [
      "Sonoma County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Windsor, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.5261714
    ],
    "lngs_derived": [
      -122.78627390643857
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862223586",
    "date_posted": "2025-09-02T11:54:10",
    "date_created": "2025-09-02T07:59:35.456144",
    "title": "Assistant Team Leader",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "6301 Hembree Lane",
          "addressLocality": "Windsor",
          "addressRegion": "CA",
          "postalCode": "95492",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17.06,
        "maxValue": 21,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541052",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Windsor"
    ],
    "counties_derived": [
      "Sonoma County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Windsor, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      38.5261714
    ],
    "lngs_derived": [
      -122.78627390643857
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nAssistant Team Leader\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nThis position requires individuals who are skilled in both supporting management operations and leading diverse teams. In the role of Assistant Team Leader, you'll aid the convenience store manager in all aspects of the store's operations—a responsibility you'll prepare for through a training sequence that teaches you our in-store retail information system, inventory management and ordering technology.\nYou will be responsible for tasks such as completing daily paperwork, troubleshooting car wash problems and addressing problems with gas pumps. Leadership duties include, but are not limited to, forecasting, ordering, stocking, merchandising, being a role-model for prompt and courteous customer service and sharing management responsibilities with the store manager.\nWe expect all our Assistant Team Leaders to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Assistant Team Leaders (this list is not all inclusive):\nPrimary Responsibilities:\nTraining and coaching new store staff\nAssisting in creating schedules in a time keeping system\nStocking products on shelves and making sure the store always looks clean and professional\nForecasting, order, stock, and merchandise products\nEnsuring prompt reconciliation of store paperwork\nEnsuring prompt, efficient, and courteous customer service to store customers, vendors, and staff\nMaintaining a clean, customer friendly environment in the store and surrounding property\nAssisting with management of store staff\nTroubleshooting and resolving car wash related issues\nFixing gas related issues, such as drive offs and the pumps being down\nAdditional duties as assigned\nRequirements and Qualifications:\nHigh School Diploma or equivalent required\nSix to nine months’ experience as an assistant manager or an equivalent combination of education and experience\nStrong mathematics ability\nStrong written and oral communication skills\nDesire to be part of a performance-driven team\nReliable transportation to and from your workplace\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nPhysical Requirements:\nThe Assistant Team Leader position requires constant standing, bending, and reaching with a moderate amount of manual dexterity. Frequent lifting of 1 to 5 pounds and occasional lifting of up to 40-50 pounds are required.\nAdditional Info:\nMust be at least 18 years of age\nMust be able to work various shifts and days of the week depending on business needs\nDisclaimer:\nThe list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$19.00 - $20.00/per hour"
  },
  {
    "id": "1862223660",
    "date_posted": "2025-09-02T11:52:09",
    "date_created": "2025-09-02T08:01:01.839566",
    "title": "Team Member",
    "organization": "Loop Neighborhood Market",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "33365 Mission Blvd.",
          "addressLocality": "Union City",
          "addressRegion": "CA",
          "postalCode": "94587",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 17,
        "maxValue": 19,
        "unitText": "HOUR"
      }
    },
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541051",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=18312",
    "cities_derived": [
      "Union City"
    ],
    "counties_derived": [
      "Alameda County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Union City, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      37.607718396603836
    ],
    "lngs_derived": [
      -122.02157605951112
    ],
    "remote_derived": false,
    "domain_derived": "loopneighborhood.com",
    "description_text": "Description\nTeam Member\n\nAbout the Company\nLoop Neighborhood Market is based in Union City, Calif., with stores and stations across California. The company was founded in 1978 and develops real estate and owns and operates gas stations with convenience stores and car washes. Loop Neighborhood Market also has a wholesale division that delivers fuel to dealer locations in the market.\nJoin Our Growing Team at Loop Neighborhood Market!\nAre you ready to be part of a dynamic, fast-growing organization that's reshaping the convenience store industry? Loop Neighborhood Market is an industry leader looking for passionate, customer-focused individuals to help us redefine the c-store experience.\nOur mission is simple: to offer high-quality, better-for-you products, paired with exceptional customer service, and create a fantastic experience from the moment you walk into our stores. If you're motivated by innovation and have a passion for delivering outstanding service, we'd love to have you on our team.\nApply today and help us change the way people experience convenience!\nPosition Summary:\nWe are looking for all levels (including entry level) of hardworking, dedicated, customer focused individuals who enjoy interacting with customers and helping make a difference in the world. We offer both full-time and part-time careers for all three shifts (first, second, or third) allowing employees the flexibility to work a schedule that best fits in with their lifestyle. Our company stives to provide employees the with opportunity to develop their skills while giving them room to grow within the organization.\nOur Team Members are responsible for ensuring the smooth operation of the station during their shift, as defined by company policy. This includes contributing to the increased profitability and growth of the store and guaranteeing our customers’ needs are met every step of the way. We empower our employees to step outside the box to offer best-in-class service to all of our customers, each and every day.\nWe expect all our Team Members to embody our Core Values: People, Teamwork, Communication, Training, Results Matter, Fun, Customer Centered and Safety. We all win as one. Living our brand is a critical component for all of our roles.\nBelow is a general outline of some of the roles and responsibilities expected of our Team Members (this list is not all inclusive):\nPrimary Responsibilities:\nManaging the cash register throughout the shift, ensuring the money stays balanced and customers are assisted in a fast and accurate manner\nStocking products on shelves and making sure the store looks clean and professional at all times\nEnsuring prompt, efficient and courteous customer service to store customers, vendors, and staff at all times\nMaintaining a clean, customer friendly environment in the store and surrounding property\nTroubleshooting and resolving car wash related issues as needed\nPreparing shift reports at the end of the shifts as per company guidelines\nCrossing and upselling store products and sales to assist in increasing store sales\nEscalating all high-priority issues to their immediate manager\nAdditional duties as assigned\nRequirements and Qualifications:\nMust be able to work a flexible schedule as needed\nCommunicate verbally and in writing with various management on store operations in a quick timeline, especially if there are any changes or items that may adversely affect the store’s operations\nAbility to read, understand, and write in the English language\nPerform basic math including proper calculation of change, etc.\nHave the ability to validate identification prior to selling tobacco and/or alcohol (as required under applicable laws and regulations)\nCan lift up to 50 pounds\nAbility to climb ladders as needed\nAbility to remain calm and respond to emergencies according to policies and procedures defined by company guidelines\nTolerate exposure to gasoline fumes and cleaning products\nAbility to work in various temperature environments (coolers, outside in various weather conditions, and in the station)\nEmployee Incentives:\nEmployees that are with us for 6 months to 3 years = 0.10 cents off a gallon of fuel\nEmployees that are with us for 3 years to 5 years = 0.30 cents off a gallon of fuel\nEmployees that are with us for 5+ years = 0.40 cents off a gallon of fuel\nMAXIMUM 20 GALLONS AND 2 FILL UPS PER WEEK\nAdditional Info:\nMust be 18+ years old to work 1st and 2nd shift\nMinimum of 21 years old to work 3rd shift\nDisclaimer: The list of requirements, duties, and responsibilities listed above is by no means a complete list. It is merely a general summary of the position described. Management reserves the right to revise or change this position description at any time.\n** The company reserves the right to run background checks as a condition of employment\nSalary Description\n$17.55 - $19.00/per hour"
  },
  {
    "id": "1862224805",
    "date_posted": "2025-09-02T11:12:09",
    "date_created": "2025-09-02T08:05:01.755318",
    "title": "Busser/Runner",
    "organization": "Zinc Cafe & Bar - Downtown Los Angeles",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "580 Mateo St",
          "addressLocality": "Los Angeles",
          "addressRegion": "CA",
          "postalCode": "90013",
          "addressCountry": "US"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": null,
    "url": "https://recruiting.paylocity.com/Recruiting/Jobs/Details/3541050",
    "source_type": "ats",
    "source": "paylocity",
    "source_domain": "recruiting.paylocity.com",
    "organization_logo": "https://recruiting.paylocity.com/recruiting/jobs/GetLogoFile?moduleId=36419",
    "cities_derived": [
      "Los Angeles"
    ],
    "counties_derived": [
      "Los Angeles County"
    ],
    "regions_derived": [
      "California"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Los Angeles, California, United States"
    ],
    "timezones_derived": [
      "America/Los_Angeles"
    ],
    "lats_derived": [
      34.03937775
    ],
    "lngs_derived": [
      -118.2325129587503
    ],
    "remote_derived": false,
    "domain_derived": "zinccafe.com",
    "description_text": "Description\nZinc is a restaurant and market that provides our employees and customers a sense of place. Anyone who walks through the doors can recharge, connect with one another and to the community in which they live. Everything we do at Zinc is done with this in mind: Simple ingredients for a good life.\n\nOur Busser/Runners are relied on to provide memorable, thoughtful experiences through engaging with our guests, serving Zinc foods with a smile and anticipating the needs of each guest that visits us. No matter what position you start in with us, you will have the opportunity to be cross-trained and will be encouraged to take on different positions within our team.\n\nResponsibilities:\nWelcome and connect with every guest, provide friendly and personable service\nFollow health, safety and sanitation guidelines\nMaintain cleanliness of the restaurant and restrooms\nLearn and maintain knowledge of all our menus & products and demonstrate knowledge of dietary/allergy information and proper food handling\nAccommodate requests from seated guests\nPromptly clean tabletops, seating and floors after each guest\nDeliver food/drinks to seated guests\nEnsure food and beverage quality and order accuracy prior to serving\nHandle varying levels of business volume with composure & a positive attitude\nPerform all opening and closing duties assigned by managers\nMaintain customer privacy, behave with open-mindedness and cultural sensitivity\nFollow all safety and state guidelines for preventing transmission of Covid-19 and other illnesses\nBenefits:\nA friendly, fun, positive work environment\nCompetitive wages plus tips; minimum starting wage is dependent on the location worked\nDiscounts on Zinc products, food & beverages\nMedical, Dental, & Vision plan options available for part time and full time Team Members\nHoliday Premium: hourly employees who work on an observed holiday will be paid 1.5x their hourly wage\n401k, company matched contribution\nJob Qualifications:\nA team player with a positive attitude\nQuick and flexible learner\nAttention to detail\nFlexibility and willingness to adapt to changes\nStrong organizational time management skills, ability to multitask\nCommunication and collaboration skills\nFluent in English\nFood handlers certification\nCovid Vaccination required\nWork Authorization: United States Citizen or Undocumented Noncitizen authorized to work in the United States\nWork Context:\nWalking and standing for long periods of time\nWorking with hot foods and beverages\nTasks will be performed using and in the proximity of coolers, stoves, and other hot equipment\nThe employee may frequently be required to stoop, kneel, and crouch for duration of shift (eight hours or longer)\nThe employee must frequently lift and/or move and/or push up to 50 pounds without assistance\nThe work environment characteristics described here are representative of those an employee encounters while performing the essential functions of this job in a typical office and restaurant environment\nReasonable accommodations may be made to enable individuals with disabilities to perform the essential functions\nPlease note this job description is not designed to cover or contain a comprehensive listing of activities, duties or responsibilities that are required of the employee for this job. Duties, responsibilities, and activities may change at any time with or without notice.\n\nZinc Café & Market is an equal opportunity employer that is committed to diversity and inclusion in the workplace. We prohibit discrimination and harassment of any kind based on race, color, sex, religion, sexual orientation, national origin, disability, genetic information, pregnancy, or any other protected characteristic as outlined by federal, state, or local laws. This policy applies to all employment practices within our organization, including hiring, recruiting, promotion, termination, layoff, recall, leave of absence, compensation, benefits, training, and apprenticeship. Zinc Café & Market makes hiring decisions based solely on qualifications, merit, and business needs at the time."
  },
  {
    "id": "1862281504",
    "date_posted": "2025-09-02T10:57:00.454",
    "date_created": "2025-09-02T10:57:04.328438",
    "title": "Infirmier (IDE) H/F",
    "organization": "Colisée France",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Pernes",
          "addressRegion": "Hauts-de-France",
          "postalCode": "62550",
          "addressCountry": "France"
        }
      }
    ],
    "locations_alt_raw": [
      "Pernes, France"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Temps partiel"
    ],
    "url": "https://jobs.smartrecruiters.com/ColiseeFrance/744000079455931-infirmier-ide-h-f",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Pernes"
    ],
    "counties_derived": [
      "Pas-de-Calais"
    ],
    "regions_derived": [
      "Hauts-de-France"
    ],
    "countries_derived": [
      "France"
    ],
    "locations_derived": [
      "Pernes, Hauts-de-France, France"
    ],
    "timezones_derived": [
      "Europe/Paris"
    ],
    "lats_derived": [
      50.4841033
    ],
    "lngs_derived": [
      2.410749
    ],
    "remote_derived": false,
    "domain_derived": "colisee.fr",
    "description_text": "Description de l'entreprise\nRejoignez l'équipe des Verrières ! \nNotre but ? Nous mettons les résidents au cœur de nos vies car ils ont l’expérience, la connaissance et sont ainsi une source d’inspiration auprès de laquelle nous continuons d’apprendre.\nNous les respectons et les considérons en portant une attention particulière à leur qualité de vie. Et c’est vous qui leur donnez les moyens de se réaliser quotidiennement à vos côtés : s’émerveiller, découvrir, entreprendre…\nChoisir notre établissement, c’est rejoindre la Communauté Colisée : des lieux de vie qui sont pleinement intégrés dans la société, ouverts sur l’extérieur et en harmonie avec le territoire.\nNotre établissement : \nL'établissement accompagne 79 résidents dont 14 en unité de vie protégée et également un Pôle d'Activités et de Soins Adaptées (PASA).\nLa résidence est proche du centre-ville de Pernes et facilement accessible en transports en commun. L'établissement est située dans un cadre paisible grâce à son parc arboré de 2 hectares. \nDescription du poste\nSe révéler chez Colisée ! \nEn rejoignant notre équipe, attendez vous à : \ndes journées nouvelles et sans routine aux côtés des résidents et des autres membres de l'équipe,\nune souplesse dans votre travail au quotidien,\ndes perspectives de carrière et des formations pour vous révéler,\nun contrat de heures à durée indéterminée,\n1 week-end travaillé sur 2.\nLe talent, c'est vous !\nVous êtes infirmier H/F diplômé et passionné.\nVous réalisez les diagnostics, soins infirmiers et activités thérapeutiques adaptés aux résidents en respectant les protocoles de soin et d’hygiène. \nVous êtes le relais des médecins pour les soins et coordonnez les auxiliaires médicaux (psychologue, aides-soignants…).\nVous participez à l’établissement du projet de soin individualisé avec l’IDEC et le médecin coordonnateur.\nVous partagez des moments complices avec eux, grâce à votre sourire, votre patience, votre bonne humeur et votre oreille attentive. \nDevenez Coliséen et faites partie d’une Communauté de Talents au service des résidents!\nQualifications\nNous ne voyons pas que votre CV en vous !\nParce que les résidents débordent d’énergie et de curiosité, vous serez choisi et reconnu pour votre personnalité et vos singularités !\nVous êtes diplômé d’Etat Infirmier et vous vous reconnaissez dans nos valeurs CORE (COhésion, Respect, Engagement).\nNous considérons chaque Talent et mettons tout en œuvre pour qu’ils puissent se révéler.\nCela passe à la fois par l’écoute, la transparence et un dialogue social continu, mais aussi par les opportunités de formation, avec notamment notre plateforme CORE Academy.\nInformations complémentaires\nTous nos postes sont ouverts aux personnes en situation de handicap. Parce que la diversité est une force, Colisée s' engage dans l'inclusion et la non-discrimination pour garantir l'égalité des chances."
  },
  {
    "id": "1862281510",
    "date_posted": "2025-09-02T10:56:58.554",
    "date_created": "2025-09-02T10:57:04.611373",
    "title": "Aushilfe Inventur – Lörrach (m/w/d)",
    "organization": "H&M Group",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Tumringer Straße 186",
          "addressLocality": "Lörrach",
          "addressRegion": "Baden-Württemberg",
          "postalCode": "79539",
          "addressCountry": "Germany"
        }
      }
    ],
    "locations_alt_raw": [
      "Tumringer Str. 186, 79539 Lörrach, Deutschland"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Teilzeit"
    ],
    "url": "https://jobs.smartrecruiters.com/HMGroup/744000079456614-aushilfe-inventur-lorrach-m-w-d-",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Lörrach (Kernstadt)"
    ],
    "counties_derived": [
      "Landkreis Lörrach"
    ],
    "regions_derived": [
      "Baden-Württemberg"
    ],
    "countries_derived": [
      "Germany"
    ],
    "locations_derived": [
      "Lörrach (Kernstadt), Baden-Württemberg, Germany"
    ],
    "timezones_derived": [
      "Europe/Berlin"
    ],
    "lats_derived": [
      47.6132768
    ],
    "lngs_derived": [
      7.6609629
    ],
    "remote_derived": false,
    "domain_derived": "hmgroup.com",
    "description_text": "Stellenbeschreibung\nDEINE ROLLE\nAls Inventuraushilfe unterstützt du unser Team bei der Inventur auf der Verkaufsfläche und im Lager.\nDeine Aufgaben:\nDu zählst und scannst die Ware im Verkaufsraum und im Lager am 22.09.2025 und am 23.09.2025 von 19:00 bis 23:59 Uhr. \nWER DU BIST​\nWir suchen Talente, die …\nüber einen längeren Zeitraum konzentriert, sorgfältig und fokussiert bleiben.\nzuverlässig sind und gerne im Team arbeiten.\nkommunikationsstark und neugierig sind mit technischen Hilfsmitteln umzugehen.\nDARUM WIRST DU ES LIEBEN, BEI UNS ZU ARBEITEN \nein attraktiver Stundenlohn von 13,48 €\neine tolle Unternehmenskultur mit offenen Türen in der Wertschätzung, Diversität und Inklusion gelebt werden\nWER WIR SIND \nDie H&M Group ist ein global agierendes Unternehmen mit starken Modemarken und innovativen Geschäftszweigen. Wir glauben daran, dass herausragendes Design, erschwingliche Preise und nachhaltige Lösungen keine Gegensätze sein müssen. Im Mittelpunkt all unserer Entscheidungen stehen unsere Kund*innen. Unsere Unternehmenskultur wird von tausenden leidenschaftlichen und talentierten Teammitgliedern geprägt. Gemeinsam nutzen wir unsere Größe und unser Wissen, um die Fashionbranche in eine inklusivere und nachhaltigere Zukunft zu führen. ​\n​WERDE TEIL UNSERES TEAMS ​\nUnsere Stärke und Einzigartigkeit liegt in vielen Dingen – in unserer inklusiven Kultur, unseren starken Werten und den Entwicklungsmöglichkeiten. Doch vor allem sind es unsere Teammitglieder, die uns zu dem machen, was wir sind.\n​Werde Teil unseres Teams und mach den nächsten Schritt in deiner Karriere mit uns – die Reise beginnt hier. ​\n* H&M ist ein Teil der H&M Group, in der wir entschlossen sind, inklusive, vielfältige und gleichberechtigte Arbeitsplätze zu schaffen und zu erhalten. Unsere Teams bestehen aus einer Vielzahl von Menschen, die ihr Wissen, ihre Erfahrung und ihre Ideen miteinander teilen und kombinieren. Vielfältige Teams wirken sich positiv auf die Art und Weise aus, wie wir Herausforderungen angehen, auf das, was wir für möglich halten, und auf die Art und Weise, wie wir mit unseren Teammitgliedern und Kund*innen auf der ganzen Welt arbeiten. Daher werden bei unserem Einstellungsprozess alle Aspekte der Vielfalt berücksichtigt. Wir bemühen uns um einen fairen und gleichberechtigten Prozess und bitten dich, deiner Bewerbung kein Anschreiben beizufügen, da diese häufig Informationen enthalten, die leicht zu unbeabsichtigten Vorurteilen führen können. Schwerbehinderte und ihnen gleichgestellte Bewerber*innen werden bei gleicher Eignung besonders berücksichtigt."
  },
  {
    "id": "1862281508",
    "date_posted": "2025-09-02T10:56:43.791",
    "date_created": "2025-09-02T10:57:04.479018",
    "title": "Dental Nurse",
    "organization": "PortmanDentex",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "17 East High Street",
          "addressLocality": "Airdrie",
          "addressRegion": "Scotland",
          "postalCode": "ML6 6LF",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "17 E High St, Airdrie ML6 6LF, UK"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Part-time"
    ],
    "url": "https://jobs.smartrecruiters.com/PortmanDentex/744000079456253-dental-nurse",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Airdrie"
    ],
    "counties_derived": [
      "North Lanarkshire"
    ],
    "regions_derived": [
      "Scotland"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Airdrie, Scotland, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      55.86870866149349
    ],
    "lngs_derived": [
      -3.982370980526168
    ],
    "remote_derived": false,
    "domain_derived": "portmandentex.com",
    "description_text": "Job Description\nAbout the role and practice \nIf you're a patient-focused Dental Nurse looking for a rewarding role in a friendly and professional environment, look no further that Bankhouse Dental Care practice in Airdrie.\nPart-time hours up to 24 hours per week\n3 days per week\n6 month fix term contract \nBankhouse Dental Care is a modern and welcoming dental practice located in the heart of Airdrie, we offer a comprehensive range of dental services for patients of all ages both NHS and private. Our team of experienced and friendly dentists, hygienists, and dental nurses are dedicated to providing high-quality, personalised care in a comfortable and relaxed environment.\nAbout you \nWe welcome your application to our Dental Nurse vacancy if you have the following skills and qualifications.\nValid certification or diploma in Dental Nursing \nRegistration with the General Dental Council (GDC) \nA positive attitude, empathy, and the ability to communicate well with patients and colleagues \nPassionate about building great relationships with patients and colleagues, and providing exceptional standards of care. \nWhat do you get in return? \nAs a PortmanDentex colleague, you’ll be part of a collaborative team that celebrates individuality. By growing together, we’ll reimagine group dentistry and wellness, enabling happier and healthier futures for all our clinicians, colleagues and patients. Ready to aim higher and join our journey? Click to apply now and discover more. \nIn addition to our benefits package also includes: \nCompetitive salary from £13.05\nGDC, Indemnity and CPD costs covered \nBonus scheme based on practice performance \nAccess to our Dental Academy to support you with your career ambitions \nAdditional special days off (such as your birthday), and the opportunity to purchase up to 3 additional annual leave days \nEnhanced maternity and paternity leave \nLife assurance and contributory pension scheme \nEmployee Assistance Programme - 24/7, 365 days a year confidential helpline and counselling service, plus 24/7 GP service \nTo apply for our Dental Nurse vacancy, you can submit your latest CV, or contact [email protected] to arrange an initial chat. Alternatively, please feel free to share this opportunity with your friends or colleagues who may be interested. \nIND001 \n#LI-XX1 \nAdditional Information\nhere\nWe are an equal opportunity employer and value diversity, equity and inclusion in our workplace. We are committed to creating an environment of mutual respect and are dedicated to providing equal employment opportunities regardless of race, religion or belief, sex, sexual orientation, gender reassignment, pregnancy or maternity, marital or civil partner status, disability, age, or nationality."
  },
  {
    "id": "1862281509",
    "date_posted": "2025-09-02T10:56:36.051",
    "date_created": "2025-09-02T10:57:04.4885",
    "title": "Software Engineer",
    "organization": "Visa",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "London",
          "addressRegion": "UNITED KINGDOM",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "London, United Kingdom"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/Visa/744000079456176-software-engineer",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "London"
    ],
    "counties_derived": [
      "Greater London"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "London, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      51.5074456
    ],
    "lngs_derived": [
      -0.1277653
    ],
    "remote_derived": false,
    "domain_derived": "visa.com",
    "description_text": "Company Description\nVisa is a world leader in payments and technology, with over 259 billion payments transactions flowing safely between consumers, merchants, financial institutions, and government entities in more than 200 countries and territories each year. Our mission is to connect the world through the most innovative, convenient, reliable, and secure payments network, enabling individuals, businesses, and economies to thrive while driven by a common purpose – to uplift everyone, everywhere by being the best way to pay and be paid.\nMake an impact with a purpose-driven industry leader. Join us today and experience Life at Visa.\nJob Description\nCurrencycloud was acquired by Visa in December 2021. Our Software Engineers are responsible for implementing an industry-leading API that has already processed over 50 billion USD of cross-border transactions for over 5 million end users, and is available to our clients 24x7. But we’re not stopping there, and our engineers are at the forefront of taking us forward to meet the demands of even greater scale. \nOur stack runs on AWS as a set of distributed applications using Kubernetes and a microservice-led architecture. We are also utilising Kafka for our streaming and PACT for Contract testing. \nWhat you'll get to do \nAs a Software Engineer you’ll play a key role within your cross functional team, taking responsibility for your services and the technology within them. \nThese roles fit in to squads who are building out brand new parts to our payments platform, focusing on high availability, cloud native, microservice concepts \nYou'll get to work as the Senior Engineer in your squad, leading on discussions around technical direction and systems design, as well as mentoring more junior members of the team \nYou'll get \nClear ownership of your domain \nA clean modern codebase \nAn independent path to production \nStrong platform and product support \nThe ability to make real changes with real business value. \nOur Tech Stack includes \nObject-oriented programming forms the bulk of our codebase, currently in Java, versions 11+, and ideally Springboot framework \nHighly-scalable, highly-available, cloud-native applications on AWS are key to our next phase of growth, are written to 12-factor principles and fit into our microservices architecture \nCloud-related tools, services, and distributed system observability to support these applications, such as Docker, Kubernetes, ElasticSearch, log management systems, and Datadog APM, to name but a few \nAPI specifications, conforming to the OpenAPI (Swagger) standard, provide a clean boundary both externally between our customers and our product, and internally between our microservices \nSQL, and large SQL databases, provide the persistence layer for our applications. You’ll be working with (and know the limitations of using) such large datastores \nInfrastructure automation is primarily owned by the infrastructure team, but you will be a consumer of their work, familiarity with AWS, Terraform and Docker is beneficial \nTesting approaches, including TDD, BDD and Contract Testing, all form an important part of our approach to quality assurance, ensuring that the code that we write forms products that are fit for use. We currently use a variety of frameworks including JUnit, RSpec and Cucumber \nAgile development, with teams broadly aligned with the Spotify - Squads and Tribes - model, helps us deliver incremental improvements to our products in an iterative manner. Advocating this model, and joining us on a journey of continuous improvement, is a key attribute of members of our teams \nContinuous Integration and Continuous Delivery pipelines allow us to automate-all-the-things, providing repeatable builds and consistent deployments \nGitHub, and the GitHub PR review process, forms a core part of our developer workflow, and peer reviews help share knowledge and improve quality \nTeamwork, and cross-team collaboration, is fundamental to the delivery of our applications. Whilst each application has an independent path to production, there will always be some activities and initiatives that span multiple teams and require cross-team collaboration. Within your team you’ll need to collaborate with a number of stakeholders, including Product Owners and QA, as part of your product development \nThis is a hybrid position. Expectation of days in office will be confirmed by your Hiring Manager.\nQualifications\nBasic Qualifications:\n2+ years of relevant work experience and a Bachelors degree, OR 5+ years of relevant work experience\n\nPreferred Qualifications:\n3 or more years of work experience with a Bachelor’s Degree or more than 2 years of work experience with an Advanced Degree (e.g. Masters, MBA, JD, MD)\n\n5+ years experience in Java Backend Development\n\nSkills with functional Java (versions 8+) and Spring (ideally Springboot)\n\nAgile ways of working such as Scrum or Kanban in cross-functional teams\n\nExpert knowledge of Docker, EKS, AWS (public cloud) and Kafka\nAdditional Information\nVisa is an EEO Employer. Qualified applicants will receive consideration for employment without regard to race, color, religion, sex, national origin, sexual orientation, gender identity, disability or protected veteran status. Visa will also consider for employment qualified applicants with criminal histories in a manner consistent with EEOC guidelines and applicable local law."
  },
  {
    "id": "1862281513",
    "date_posted": "2025-09-02T10:56:33.178",
    "date_created": "2025-09-02T10:57:04.833067",
    "title": "Senior Lighting Engineer",
    "organization": "AECOM",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Chesterfield",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      " Nottingham, United Kingdom"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/AECOM2/744000079456505-senior-lighting-engineer",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Nottingham"
    ],
    "counties_derived": [
      "Nottinghamshire"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Nottingham, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      52.9534193
    ],
    "lngs_derived": [
      -1.1496461
    ],
    "remote_derived": false,
    "domain_derived": "aecom.com",
    "description_text": "Company Description\nWork with Us. Change the World.\nAt AECOM, we're delivering a better world. Whether improving your commute, keeping the lights on, providing access to clean water, or transforming skylines, our work helps people and communities thrive. We are the world's trusted infrastructure consulting firm, partnering with clients to solve the world’s most complex challenges and build legacies for future generations.\nThere has never been a better time to be at AECOM. With accelerating infrastructure investment worldwide, our services are in great demand. We invite you to bring your bold ideas and big dreams and become part of a global team of over 50,000 planners, designers, engineers, scientists, digital innovators, program and construction managers and other professionals delivering projects that create a positive and tangible impact around the world.\nWe're one global team driven by our common purpose to deliver a better world. Join us.\nJob Description\nStart here. Grow here. \nOur Lighting Team is seeking a Senior Lighting Engineer to drive the future of lighting across the UK. This role offers an exciting opportunity to influence infrastructure projects from conception through completion.\nEach team member has a development plan to provide a clear pathway to personal development and career progression. The team provides technical leadership of projects throughout the infrastructure lifecycle from feasibility, preliminary and detailed stage designs in some cases through construction.\nOur clients are many and varied from the private and public sector working with numerous local authorities, we work with internal client from transport, rail etc.\nHere’s what you’ll do:\nDevelop: Manage engineering tasks, explore subject areas, define project scopes, and create unique solutions.\nAdvise: Provide expert technical knowledge and support across multi-disciplinary projects.\nDesign: from conceptual stages to implementation which will include site visits, lighting designs, private cable calculation designs, CAD designs, production of lighting specifications, Bills of Quantities and liaison with DNO suppliers.\nEnsure Quality: Strong efficiencies on quality and budget control on projects, navigate the complexities of transportation and landscape projects, working with clients to address and resolve challenges.\nCollaborate: Build strong relationships with technical teams and clients, leading multi-disciplinary efforts to achieve integrated design solutions.\nCome grow with us:\nAnd let's not forget about the perks at AECOM. You'll enjoy a range of core and personalised benefits designed to support your future and well-being, customized to fit your lifestyle. Take advantage of career development opportunities, our flexible hybrid working model to ensure a work-life balance that suits your lifestyle, technical practice networks, AECOM University, and volunteering days. \nQualifications\nReady to push the limits of what’s possible? \nRequirements:\nRelevant Technical Qualifications: Ideally, you possess an ILP Exterior Lighting Diploma or equivalent qualification in a related technical field.\nProven Design Experience: Demonstrated success in a lighting design environment, with a proactive and creative approach to problem-solving.\nSoftware Proficiency: Proficient in industry-standard software, including Lighting Reality, AGi32, Dialux, and Amtech Pro Design to create and assess detailed lighting schemes.\nStrong Communication and Interpersonal Skills: Exceptional written and verbal communication skills, with the ability to confidently and diplomatically engage with staff, colleagues, and clients.\nProject Management: Oversee project timelines, budgets, and resources to ensure projects are delivered on schedule, within budget, and to the highest quality standards. Manage client expectations and project requirements from inception through to completion.\nAdditional Information\nAt AECOM, we value everyone's unique contributions and perspectives. If you meet some of the requirements above or have transferable skills you believe would benefit us, we would be delighted to hear from you!\nInterested in the role or curious about life at AECOM? Follow us on LinkedIn, Facebook, Instagram, and YouTube to explore our AECOM voices, employee stories, latest projects, and much more! \nWorking locations is flexible across the UK (Hybrid - office/remote working), while attendance will be required a nearest local office from time to time (minimum once a week).\nAbout AECOM\nAECOM is the world’s trusted infrastructure consulting firm, delivering professional services throughout the project lifecycle – from advisory, planning, design and engineering to program and construction management. On projects spanning transportation, buildings, water, new energy and the environment, our public- and private-sector clients trust us to solve their most complex challenges. Our teams are driven by a common purpose to deliver a better world through our unrivaled technical and digital expertise, a culture of equity, diversity and inclusion, and a commitment to environmental, social and governance priorities. AECOM is a Fortune 500 firm and its Professional Services business had revenue of $14.4 billion in fiscal year 2023. See how we are delivering sustainable legacies for generations to come at aecom.com and @AECOM.\nFreedom to Grow in a World of Opportunity \nYou will have the flexibility you need to do your best work with hybrid work options. Whether you’re working from an AECOM office, remote location or at a client site, you will be working in a dynamic environment where your integrity, entrepreneurial spirit and pioneering mindset are championed.\nYou will help us foster a safe and respectful workplace, where we invite everyone to bring their whole selves to work using their unique talents, backgrounds and expertise to create transformational outcomes for our clients.\nAECOM provides a wide array of compensation, benefits and well-being programs to meet the diverse needs of our employees and their families. We’re the world’s trusted global infrastructure firm, and we’re in this together – your growth and success are ours too.\nJoin us, and you’ll get all the benefits of being a part of a global, publicly traded firm – access to industry-leading technology and thinking and transformational work with big impact and work flexibility. As an Equal Opportunity Employer, we believe in each person’s potential, and we’ll help you reach yours.\nWe are a Disability Confident Employer and will offer an interview to applicants who have a disability or long-term condition, who meet the minimum/essential criteria for the role. Please let us know using this email address [email protected] if you would like to apply through the Disability Confident Interview Scheme.\nAll your information will be kept confidential according to EEO guidelines."
  },
  {
    "id": "1862281511",
    "date_posted": "2025-09-02T10:56:09.274",
    "date_created": "2025-09-02T10:57:04.671863",
    "title": "Employé Polyvalent H/F",
    "organization": "Groupement Les Mousquetaires",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "41 Rue Jacques Offenbach",
          "addressLocality": "Saint-Nazaire",
          "addressRegion": "Pays de la Loire",
          "postalCode": "44600",
          "addressCountry": "France"
        }
      }
    ],
    "locations_alt_raw": [
      "41 Rue Jacques Offenbach, 44600 Saint-Nazaire, France"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Temps complet"
    ],
    "url": "https://jobs.smartrecruiters.com/GroupementLesMousquetaires/744000079456455-employe-polyvalent-h-f",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Saint-Nazaire"
    ],
    "counties_derived": [
      "Loire-Atlantique"
    ],
    "regions_derived": [
      "Pays de la Loire"
    ],
    "countries_derived": [
      "France"
    ],
    "locations_derived": [
      "Saint-Nazaire, Pays de la Loire, France"
    ],
    "timezones_derived": [
      "Europe/Paris"
    ],
    "lats_derived": [
      47.2635206
    ],
    "lngs_derived": [
      -2.2382171
    ],
    "remote_derived": false,
    "domain_derived": "mousquetaires.com",
    "description_text": "Description de l'entreprise\nLe Groupement Les Mousquetaires, ce sont 7 enseignes de la grande distribution, 150 000 collaborateurs et plus de 3 000 chefs d’entreprise indépendants !\nIntermarché & Netto fait du mieux manger accessible à tous une réalité. Notre indépendance et la diversité de nos métiers nous permettent de répondre aux attentes des Français et nous propulsent au rang de 3e distributeur. Chaque métier compte pour écrire l’avenir de la distribution alimentaire.\nPrêt.e à faire la différence ? Rejoignez-nous !\nDescription du poste\nPossédant une forte adaptabilité et aimant la polyvalence, vous serez amené à être un soutien pour l'équipe boulangerie.\nSavoir gérer son temps, les priorités, et adapter son travail en fonction de l'afflux clients sont des avantages.\nQualifications\nDébutant accepté. Dynamisme recommandé. Esprit d'équipe.\nInformations complémentaires\nVenez rejoindre une équipe dynamique dans un cadre familial. CDI à temps partiel 26h/semaine."
  },
  {
    "id": "1862281506",
    "date_posted": "2025-09-02T10:55:53.603",
    "date_created": "2025-09-02T10:57:04.375325",
    "title": "Senior Lighting Engineer",
    "organization": "AECOM",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Chesterfield",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "London, United Kingdom"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/AECOM2/744000079456405-senior-lighting-engineer",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "London"
    ],
    "counties_derived": [
      "Greater London"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "London, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      51.5074456
    ],
    "lngs_derived": [
      -0.1277653
    ],
    "remote_derived": false,
    "domain_derived": "aecom.com",
    "description_text": "Company Description\nWork with Us. Change the World.\nAt AECOM, we're delivering a better world. Whether improving your commute, keeping the lights on, providing access to clean water, or transforming skylines, our work helps people and communities thrive. We are the world's trusted infrastructure consulting firm, partnering with clients to solve the world’s most complex challenges and build legacies for future generations.\nThere has never been a better time to be at AECOM. With accelerating infrastructure investment worldwide, our services are in great demand. We invite you to bring your bold ideas and big dreams and become part of a global team of over 50,000 planners, designers, engineers, scientists, digital innovators, program and construction managers and other professionals delivering projects that create a positive and tangible impact around the world.\nWe're one global team driven by our common purpose to deliver a better world. Join us.\nJob Description\nStart here. Grow here. \nOur Lighting Team is seeking a Senior Lighting Engineer to drive the future of lighting across the UK. This role offers an exciting opportunity to influence infrastructure projects from conception through completion.\nEach team member has a development plan to provide a clear pathway to personal development and career progression. The team provides technical leadership of projects throughout the infrastructure lifecycle from feasibility, preliminary and detailed stage designs in some cases through construction.\nOur clients are many and varied from the private and public sector working with numerous local authorities, we work with internal client from transport, rail etc.\nHere’s what you’ll do:\nDevelop: Manage engineering tasks, explore subject areas, define project scopes, and create unique solutions.\nAdvise: Provide expert technical knowledge and support across multi-disciplinary projects.\nDesign: from conceptual stages to implementation which will include site visits, lighting designs, private cable calculation designs, CAD designs, production of lighting specifications, Bills of Quantities and liaison with DNO suppliers.\nEnsure Quality: Strong efficiencies on quality and budget control on projects, navigate the complexities of transportation and landscape projects, working with clients to address and resolve challenges.\nCollaborate: Build strong relationships with technical teams and clients, leading multi-disciplinary efforts to achieve integrated design solutions.\nCome grow with us:\nAnd let's not forget about the perks at AECOM. You'll enjoy a range of core and personalised benefits designed to support your future and well-being, customized to fit your lifestyle. Take advantage of career development opportunities, our flexible hybrid working model to ensure a work-life balance that suits your lifestyle, technical practice networks, AECOM University, and volunteering days. \nQualifications\nReady to push the limits of what’s possible? \nRequirements:\nRelevant Technical Qualifications: Ideally, you possess an ILP Exterior Lighting Diploma or equivalent qualification in a related technical field.\nProven Design Experience: Demonstrated success in a lighting design environment, with a proactive and creative approach to problem-solving.\nSoftware Proficiency: Proficient in industry-standard software, including Lighting Reality, AGi32, Dialux, and Amtech Pro Design to create and assess detailed lighting schemes.\nStrong Communication and Interpersonal Skills: Exceptional written and verbal communication skills, with the ability to confidently and diplomatically engage with staff, colleagues, and clients.\nProject Management: Oversee project timelines, budgets, and resources to ensure projects are delivered on schedule, within budget, and to the highest quality standards. Manage client expectations and project requirements from inception through to completion.\nAdditional Information\nAt AECOM, we value everyone's unique contributions and perspectives. If you meet some of the requirements above or have transferable skills you believe would benefit us, we would be delighted to hear from you!\nInterested in the role or curious about life at AECOM? Follow us on LinkedIn, Facebook, Instagram, and YouTube to explore our AECOM voices, employee stories, latest projects, and much more! \nWorking locations is flexible across the UK (Hybrid - office/remote working), while attendance will be required a nearest local office from time to time (minimum once a week).\nAbout AECOM\nAECOM is the world’s trusted infrastructure consulting firm, delivering professional services throughout the project lifecycle – from advisory, planning, design and engineering to program and construction management. On projects spanning transportation, buildings, water, new energy and the environment, our public- and private-sector clients trust us to solve their most complex challenges. Our teams are driven by a common purpose to deliver a better world through our unrivaled technical and digital expertise, a culture of equity, diversity and inclusion, and a commitment to environmental, social and governance priorities. AECOM is a Fortune 500 firm and its Professional Services business had revenue of $14.4 billion in fiscal year 2023. See how we are delivering sustainable legacies for generations to come at aecom.com and @AECOM.\nFreedom to Grow in a World of Opportunity \nYou will have the flexibility you need to do your best work with hybrid work options. Whether you’re working from an AECOM office, remote location or at a client site, you will be working in a dynamic environment where your integrity, entrepreneurial spirit and pioneering mindset are championed.\nYou will help us foster a safe and respectful workplace, where we invite everyone to bring their whole selves to work using their unique talents, backgrounds and expertise to create transformational outcomes for our clients.\nAECOM provides a wide array of compensation, benefits and well-being programs to meet the diverse needs of our employees and their families. We’re the world’s trusted global infrastructure firm, and we’re in this together – your growth and success are ours too.\nJoin us, and you’ll get all the benefits of being a part of a global, publicly traded firm – access to industry-leading technology and thinking and transformational work with big impact and work flexibility. As an Equal Opportunity Employer, we believe in each person’s potential, and we’ll help you reach yours.\nWe are a Disability Confident Employer and will offer an interview to applicants who have a disability or long-term condition, who meet the minimum/essential criteria for the role. Please let us know using this email address [email protected] if you would like to apply through the Disability Confident Interview Scheme.\nAll your information will be kept confidential according to EEO guidelines."
  },
  {
    "id": "1862281505",
    "date_posted": "2025-09-02T10:55:34.948",
    "date_created": "2025-09-02T10:57:04.354664",
    "title": "Territory Business Manager",
    "organization": "Dr Reddy's Laboratories Limited",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Chennai",
          "addressRegion": "Tamil Nadu",
          "addressCountry": "India"
        }
      }
    ],
    "locations_alt_raw": [
      "Chennai, Tamil Nadu, India"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/DrReddysLaboratoriesLimited/744000079455836-territory-business-manager",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Chennai"
    ],
    "counties_derived": null,
    "regions_derived": [
      "Tamil Nadu"
    ],
    "countries_derived": [
      "India"
    ],
    "locations_derived": [
      "Chennai, Tamil Nadu, India"
    ],
    "timezones_derived": [
      "Asia/Kolkata"
    ],
    "lats_derived": [
      13.0836939
    ],
    "lngs_derived": [
      80.270186
    ],
    "remote_derived": false,
    "domain_derived": "drreddys.com",
    "description_text": "Company Description\nDr. Reddy’s Laboratories Ltd. is a leading multinational pharmaceutical company based across global locations. Each of our 24,000 plus employees comes to work every day for one collective purpose: to accelerate access to affordable and innovative medicines because Good Health Can’t Wait.\nWe started in 1984 with a modest investment, 20 employees and a bold vision. Today, we have research and development centres, manufacturing facilities or a commercial presence in 66 countries. \nFor nearly four decades, we have stood for access, affordability and innovation based on the bedrock of deep science, progressive people practices and robust corporate governance. As the pharmaceutical industry evolves and undergoes disruption, we see an opportunity – to strengthen our core further (the next steps) and to build the future (the new bets).\n‘The Next and the New’ is how we aim to continue to be the partner of choice – purpose-driven, future-ready and sustainable. Our aim is to reach over 1.5 Bn+ patients across the world by 2030 by growing our core businesses and building for the future with sustainability at the core of our purpose and strategy. Sustainability for us means operating in a manner that respects people, planet and purpose – helping us conserve precious resources, serve our patients, create value for stakeholders, give back to society, fulfil our potential and maintain our integrity and transparency\nDr Reddy’s maintains a work environment, free from discrimination and is an equal opportunity employer. We are committed to employ & nurture all qualified diverse workforce without regard to race, colour religion, nationality, sex, age, disability status, genetics, sexual orientation, gender expression, citizenship or any other characteristic or classification protected by applicable law(s) of the country we operate in. We treasure every talent, and recognize merit and diversity in our organization.\nAdditional Information\nAbout the Department\nGlobal Generics India\nGlobal Generics India business journey began in 1986. In the last three decades, we have grown as a trusted name in the healthcare industry and rank as one of the top 10 Pharma Companies in the Indian Pharma Market (IPM) as per IQVIA MAT (November 2022). Our commitment to Lead Ahead has helped us move ranks from 16th position to 10th position (IPM) in the last four years. We are a fast-growing organisation with double-digit growth and significant market share in domestic markets. Currently, we rank among the top 5 in oncology, anti-allergy and gastrointestinal diseases and the top 10 in a few other therapy areas. Our focus is on leveraging our digital capabilities, collaborations, innovations and inorganic opportunities to become the top 5 companies in the Indian Pharma Market.\n\nBenefits Offered\nAt Dr. Reddy’s we actively help to catalyse your career growth and professional development through personalised learning programs.\nThe benefits you will enjoy at Dr. Reddy’s are on par with the best industry standards. They include, among other things and other essential equipment, joining & relocation support, family support (Maternity & Paternity benefits), learning and development opportunities, medical coverage for yourself and your family, life coverage for yourself.\n\nOur Work Culture\nAsk any employee at Dr. Reddy’s why they come to work every day and they’ll say, because Good Health Can’t Wait. This is our credo as well as the guiding principle behind all our actions. We see healthcare solutions not only as scientific formulations, but as a means to help patients lead healthier lives, and we’re always attuned to the new and the next to empower people to stay fit. And to do this, we foster a culture of empathy and dynamism. People are at the core of our journey over the last few decades. They have been supported by an enabling environment that buoys individual ability while fostering teamwork and shared success. We believe that when people with diverse skills are bound together by a common purpose and value system, they can make magic.\nFor more details, please visit our career website at https://careers.drreddys.com/#!/"
  },
  {
    "id": "1862281512",
    "date_posted": "2025-09-02T10:55:13.755",
    "date_created": "2025-09-02T10:57:04.757809",
    "title": "Global Director,  Partner Operations & Excellence",
    "organization": "IFS",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Staines-upon-Thames",
          "addressRegion": "England",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "Staines-upon-Thames, UK"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/IFS1/744000079456136-global-director-partner-operations-excellence-",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Staines-upon-Thames"
    ],
    "counties_derived": [
      "Surrey"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Staines-upon-Thames, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      51.434012
    ],
    "lngs_derived": [
      -0.511044
    ],
    "remote_derived": false,
    "domain_derived": "ifs.com",
    "description_text": "Company Description\nIFS is a billion-dollar revenue company with 7000+ employees on all continents. Our leading AI technology is the backbone of our award-winning enterprise software solutions, enabling our customers to be their best when it really matters–at the Moment of Service™. Our commitment to internal AI adoption has allowed us to stay at the forefront of technological advancements, ensuring our colleagues can unlock their creativity and productivity, and our solutions are always cutting-edge.\nAt IFS, we’re flexible, we’re innovative, and we’re focused not only on how we can engage with our customers but on how we can make a real change and have a worldwide impact. We help solve some of society’s greatest challenges, fostering a better future through our agility, collaboration, and trust.\nWe celebrate diversity and understand our responsibility to reflect the diverse world we work in. We are committed to promoting an inclusive workforce that fully represents the many different cultures, backgrounds, and viewpoints of our customers, our partners, and our communities. As a truly international company serving people from around the globe, we realize that our success is tantamount to the respect we have for those different points of view.\nBy joining our team, you will have the opportunity to be part of a global, diverse environment; you will be joining a winning team with a commitment to sustainability; and a company where we get things done so that you can make a positive impact on the world.\nWe’re looking for innovative and original thinkers to work in an environment where you can #MakeYourMoment so that we can help others make theirs. With the power of our AI-driven solutions, we empower our team to change the status quo and make a real difference.\nIf you want to change the status quo, we’ll help you make your moment. Join Team Purple. Join IFS.\nJob Description\nWe are seeking an experienced and strategic Global Director of Partner Operations & Excellence to lead the operational backbone of our rapidly scaling and diverse global partner ecosystem. This critical role will be instrumental in designing, optimizing, and scaling the systems, tools, and processes that drive partner engagement, enable partner success, and ensure operational excellence across our partner ecosystem.\nIf you are a results-oriented leader with a passion for optimizing complex partnership operations in a fast-paced, global software environment, and building a world-class partner experience, we encourage you to apply.\nKey Responsibilities\nGlobal Partner Program Design & Governance:\nAlign with our Global head of Programs to, implement, and continuously optimize the global framework for all partner programs including tiering models, benefits, requirements, and compliance policies, ensuring competitiveness and strategic alignment.\nOversee the development and management of our partner agreements and policy documentation, ensuring legal and financial compliance across regions and partner types.\nEstablish and enforce consistent global rules of engagement for all partnership types to minimize conflict and maximize mutual value.\nOperational Systems, Tools & Process Optimization (Partner Excellence Function):\nOwn the strategic vision, ongoing administration, and continuous optimization of our core Partner Relationship Management (PRM) system as the central operational hub for our global partner ecosystem to create a unified and automated partner operational environment.\nEvaluate, recommend, and implement new technologies and tools to enhance partner program delivery and operational efficiency and the \"Ease of Doing Business\" for our partners.\nPerformance Measurement, Reporting & Actionable Analytics:\nDefine, track, and report on key partnership performance metrics across all partner types (e.g., partner-sourced revenue, pipeline, solution implementations, joint development, partner activity, certification growth, MDF ROI, partner satisfaction).\nDevelop and manage the automated reporting infrastructure, creating comprehensive dashboards and performance insights for channel leadership, regional teams, and executive management.\nEstablish and maintain robust data governance standards for all partner-related information, ensuring data quality and reliability across global operations\nOperational Enablement & Partner Experience:\nCollaborate closely with partner enablement teams to operationalize the delivery of training materials, certification programs, and access to partner-facing tools and resources.\nDesign and implement efficient internal and external support mechanisms (e.g., helpdesk, knowledge base) to resolve operational inquiries from partners and internal stakeholders promptly.\nChampion initiatives focused on improving the overall \"Ease of Doing Business\" for partners through operational improvements and simplified processes.\nQualifications\n10+ years of progressive experience in Partner Operations, Alliance Operations, Business Operations, or related functions within the enterprise software (ERP preferred), SaaS, or B2B technology sector.\n5+ years in a global or regional leadership role, managing complex operations across diverse geographies and partner types.\nDemonstrable expertise in designing, implementing, and managing global partner programs, policies, and operational frameworks.\nDeep practical experience with Partner Relationship Management (PRM) systems (e.g., Salesforce PRM, Impartner, Allbound) and their strategic integration with CRM (Salesforce, Microsoft Dynamics 365) and ERP (IFS Cloud) platforms.\nExceptional analytical skills with a proven ability to define KPIs, develop insightful dashboards, and extract actionable insights from large datasets to drive strategic decisions.\nProven ability to lead complex, cross-functional projects, drive significant process improvements, and manage large-scale change initiatives in a dynamic, global environment.\nAdditional Information\nWe embrace flexibility and hybrid work opportunities to support diverse needs and lifestyles, while also valuing inclusive workplace experiences. By fostering a sense of community, we drive innovation, strengthen connections, and nurture belonging. Our commitment ensures you can work in a way that suits you best, while also engaging with colleagues to share ideas and build meaningful relationships."
  },
  {
    "id": "1862281507",
    "date_posted": "2025-09-02T10:54:43.409",
    "date_created": "2025-09-02T10:57:04.385993",
    "title": "HR Assistant",
    "organization": "Kanadevia Inova",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Ascent 4, Farnborough Aerospace Centre",
          "addressLocality": "Farnborough",
          "addressRegion": "England",
          "postalCode": "GU14 6XW ",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "Ascent 4, Farnborough Aerospace Centre, Farnborough, England, United Kingdom"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/KanadeviaInova/744000079456215-hr-assistant",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": null,
    "counties_derived": null,
    "regions_derived": null,
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      51.273549
    ],
    "lngs_derived": [
      -0.765276
    ],
    "remote_derived": false,
    "domain_derived": "kanadevia-inova.com",
    "description_text": "Company Description\nWelcome to Kanadevia Inova, a global innovation leader in the waste infrastructure space, where we believe in creating a sustainable future through technology and innovation.\n\nTransforming Waste into Value\n\nAt Kanadevia Inova, we pride ourselves on being at the forefront of waste-to-X technology. We are not just waste managers; we are creators of value from what communities discard. Your role at Kanadevia Inova directly contributes to turning something once considered useless - waste - into something invaluable: energy, heat, hydrogen, fertilizer, and beyond..\n\nFind out more about Kanadevia Inova at www.kanadevia-inova.com.\nJob Description\nWe’re looking for a proactive HR Assistant to join our People & Culture team in Farnborough.\nYou’ll support day-to-day HR operations, acting as the first point of contact for employees and managers, while gaining exposure to onboarding, payroll, and wider HR initiatives.\nApplicants must already have the legal right to work in the UK.\nKey Responsibilities\nProvide advice and guidance on HR and personnel matters, ensuring consistent interpretation and implementation of policies.\nDraft and issue HR-related correspondence, such as contracts, letters, and compliance documentation.\nMaintain accurate employee records, including starters, leavers, payroll data, work history, and disciplinary documentation.\nAssist with HR services including training, travel, compliance, and administration, while supporting wider HR initiatives.\nProvide HR and payroll administrative support to ensure accurate and timely processing.\nQualifications\nHR experience with knowledge of UK employment law.\nStrong MS Office skills (Excel, Word, Outlook).\nOrganised, detail-focused, and solution-oriented.\nConfident communicator with great interpersonal skills.\nPayroll experience desirable.\nAdditional Information\nAnnual salary review & bonus scheme.\nPension scheme, life insurance, private healthcare and dental insurance\nHybrid working: 3 days office, 2 days working from home\nTeam-oriented working atmosphere in an international green tech company\nFor HR agencies: Please note that we do not accept applications coming from agencies. Thank you."
  },
  {
    "id": "1862281514",
    "date_posted": "2025-09-02T10:54:43.127",
    "date_created": "2025-09-02T10:57:07.012421",
    "title": "Senior Software Engineer",
    "organization": "Williams Racing",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Grove",
          "addressRegion": "England",
          "postalCode": "OX12",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "Grove, UK"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/WilliamsRacing/744000079456205-senior-software-engineer",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Grove"
    ],
    "counties_derived": [
      "Oxfordshire"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Grove, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      51.6075105
    ],
    "lngs_derived": [
      -1.4253498
    ],
    "remote_derived": false,
    "domain_derived": "williamsf1.com",
    "description_text": "Company Description\nFor almost 50 years, Williams Racing has been at the forefront of one of the fastest sports on the planet, being one of the top three most successful teams in history competing in the FIA Formula 1 World Championship. With an almost unrivalled heritage of engineering and racing F1 cars and unforgettable eras that demonstrate it is a force to be reckoned with, the British squad boasts 16 F1 World Championship titles to its name. \nSince its foundation in 1977 by the eminent, late Sir Frank Williams and engineering pioneer Sir Patrick Head, the team has won nine Constructors’ Championships, in association with Cosworth, Honda and Renault. Its roll call of drivers is legendary, with its seven Drivers’ Championship trophies being lifted by true icons of the sport: Alan Jones, Keke Rosberg, Nelson Piquet, Nigel Mansell, Alain Prost, Damon Hill and Jacques Villeneuve. The team has made history before and is out to make it again with a long-term mission to evolve and return to the front of the grid.\nJob Description\nAt Atlassian Williams Racing, we’re seeking a Senior Software Engineer with a proven track record of solving difficult technical problems. You will have experience building scalable and performant systems, balancing short term incremental wins against long term architectural improvements. \nThis is a hands-on role focused on enabling cutting-edge simulation, modelling, and real-time analysis systems critical to our competitive edge in Formula 1. You’ll work with a highly specialized user base including race engineers, vehicle dynamics engineers, and performance analysts, helping to design and optimize software that powers everything from vehicle simulations to trackside decision-making tools. \nWe believe data and compute-intensive software are core to our performance evolution, and your work will help us move faster and smarter — both virtually and physically. \nWhat You’ll Be Doing: \nDesigning and implementing high-performance software components for simulation, data analysis, and operational decision support \nCollaborating with domain experts to encode physical models, algorithms, and workflows into robust, maintainable code \nExtending existing codebases and building new tools that scale with complex engineering workloads \nContributing to our real-time data infrastructure, including protocols for low-latency messaging and efficient data serialisation \nMentoring developers and promoting software engineering best practices in a high-integrity, performance-critical environment \nSupporting race and test events with software expertise as required \nOur Software Stack: \nWe use the right tool for the job. Our current stack includes: \nC++, Rust and C# for high-performance desktop and backend applications \nTypescript/React for web-based UIs \nPython for analysis, tooling, and rapid prototyping \nCloud-native services (Azure, Docker, Kubernetes) alongside HPC and on-prem systems \nData transport via WebSockets, TCP, and custom protocols for real-time telemetry and control \nYou’ll Be a Great Fit If You Have: \nA degree in Computer Science, Engineering, Physics, Applied Mathematics or similar \nExperience of software development, testing, and CI in languages such as C++, Rust or C#, built upon a solid foundation in computing fundamentals – OS, CPUs, memory, networking \nA problem solving and adaptable mindset, a curiosity to understand how things work, and enthusiasm to learn new techniques and technologies. \nA passion for performance profiling, debugging, and squeezing the most out of CPU and memory \nAbility to work closely with engineers and scientists to translate complex requirements into well-structured software \nA track record of driving technical decision making, bringing fresh insight and perspective on problems\nAdditional Information\n#LI-KW1\nAtlassian Williams Racing is an equal opportunity employer that values diversity and inclusion. We are happy to discuss reasonable job adjustments."
  },
  {
    "id": "1862281519",
    "date_posted": "2025-09-02T10:54:23.899",
    "date_created": "2025-09-02T10:57:07.368502",
    "title": "Senior Software Engineer",
    "organization": "Visa",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "London",
          "addressRegion": "UNITED KINGDOM",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "London, United Kingdom"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/Visa/744000079456165-senior-software-engineer",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "London"
    ],
    "counties_derived": [
      "Greater London"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "London, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      51.5074456
    ],
    "lngs_derived": [
      -0.1277653
    ],
    "remote_derived": false,
    "domain_derived": "visa.com",
    "description_text": "Company Description\nVisa is a world leader in payments and technology, with over 259 billion payments transactions flowing safely between consumers, merchants, financial institutions, and government entities in more than 200 countries and territories each year. Our mission is to connect the world through the most innovative, convenient, reliable, and secure payments network, enabling individuals, businesses, and economies to thrive while driven by a common purpose – to uplift everyone, everywhere by being the best way to pay and be paid.\nMake an impact with a purpose-driven industry leader. Join us today and experience Life at Visa.\nJob Description\nCurrencycloud was acquired by Visa in December 2021. Our Senior Software Engineers are responsible for implementing an industry-leading API that has already processed over 50 billion USD of cross-border transactions for over 5 million end users, and is available to our clients 24x7. But we’re not stopping there, and our engineers are at the forefront of taking us forward to meet the demands of even greater scale. \nOur stack runs on AWS as a set of distributed applications using Kubernetes and a microservice-led architecture. We are also utilising Kafka for our streaming and PACT for Contract testing. \nWhat you'll get to do \nAs a Senior Software Engineer you’ll play a key role within your cross functional team, taking responsibility for your services and the technology within them. \nThese roles fit in to squads who are building out brand new parts to our payments platform, focusing on high availability, cloud native, microservice concepts \nYou'll get to work as the Lead Engineer in your squad, leading on discussions around technical direction and systems design, as well as mentoring more junior members of the team \nYou'll get \nClear ownership of your domain \nA clean modern codebase \nAn independent path to production \nStrong platform and product support \nThe ability to make real changes with real business value. \nOur Tech Stack includes \nObject-oriented programming forms the bulk of our codebase, currently in Java, versions 11+, and ideally Springboot framework \nHighly-scalable, highly-available, cloud-native applications on AWS are key to our next phase of growth, are written to 12-factor principles and fit into our microservices architecture \nCloud-related tools, services, and distributed system observability to support these applications, such as Docker, Kubernetes, ElasticSearch, log management systems, and Datadog APM, to name but a few \nAPI specifications, conforming to the OpenAPI (Swagger) standard, provide a clean boundary both externally between our customers and our product, and internally between our microservices \nSQL, and large SQL databases, provide the persistence layer for our applications. You’ll be working with (and know the limitations of using) such large datastores \nInfrastructure automation is primarily owned by the infrastructure team, but you will be a consumer of their work, familiarity with AWS, Terraform and Docker is beneficial \nTesting approaches, including TDD, BDD and Contract Testing, all form an important part of our approach to quality assurance, ensuring that the code that we write forms products that are fit for use. We currently use a variety of frameworks including JUnit, RSpec and Cucumber \nAgile development, with teams broadly aligned with the Spotify - Squads and Tribes - model, helps us deliver incremental improvements to our products in an iterative manner. Advocating this model, and joining us on a journey of continuous improvement, is a key attribute of members of our teams \nContinuous Integration and Continuous Delivery pipelines allow us to automate-all-the-things, providing repeatable builds and consistent deployments \nGitHub, and the GitHub PR review process, forms a core part of our developer workflow, and peer reviews help share knowledge and improve quality \nTeamwork, and cross-team collaboration, is fundamental to the delivery of our applications. Whilst each application has an independent path to production, there will always be some activities and initiatives that span multiple teams and require cross-team collaboration. Within your team you’ll need to collaborate with a number of stakeholders, including Product Owners and QA, as part of your product development \nThis is a hybrid position. Expectation of days in office will be confirmed by your Hiring Manager.\nQualifications\nBasic Qualifications:\n5+ years of relevant work experience with a Bachelor’s Degree or at least 2 years of work experience with an Advanced degree (e.g. Masters, MBA, JD, MD) or 0 years of work experience with a PhD, OR 8+ years of relevant work experience.\n\n\nPreferred Qualifications:\n5+ years experience in Java Backend Development\n\nSkills with functional Java (versions 8+) and Spring (ideally Springboot)\n\nAgile ways of working such as Scrum or Kanban in cross-functional teams\n\nExpert knowledge of Docker, EKS, AWS (public cloud) and Kafka\n\nAbility to communicate equally effectively with both technical and non-technical stakeholders\n\nModern Cloud-Native architectures and practices. To name some: high-availability, high-scalability, microservices, 12-factor apps, CI/CD, heavy testing automation and observability.\n\nTDD, BDD and Contract testing.\n\nWorking in a DevOps environment, or passion and willingness to work in this way.\n\nProven delivery of well-tested, scalable, fault-tolerant and performant solutions.\n\nA pragmatic approach to solutions and delivery of technical projects.\n\nA self-starter who takes accountability for getting things done.\n\nPragmatism in decision making and ability to get buy-in for ideas and getting them done.\n\nExceptional structure and attention to detail.\n\nComfortable challenging the status quo and always curious about the way things work.\n\nGreat written and verbal communication skills.\n\nComfortable working in a scale-up or growth environment and as part of a wider team\nAdditional Information\nVisa is an EEO Employer. Qualified applicants will receive consideration for employment without regard to race, color, religion, sex, national origin, sexual orientation, gender identity, disability or protected veteran status. Visa will also consider for employment qualified applicants with criminal histories in a manner consistent with EEOC guidelines and applicable local law."
  },
  {
    "id": "1862281515",
    "date_posted": "2025-09-02T10:53:59.804",
    "date_created": "2025-09-02T10:57:07.091804",
    "title": "Senior Lighting Engineer",
    "organization": "AECOM",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Chesterfield",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "Birmingham, United Kingdom"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/AECOM2/744000079455603-senior-lighting-engineer",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Birmingham"
    ],
    "counties_derived": [
      "West Midlands"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Birmingham, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      52.4796992
    ],
    "lngs_derived": [
      -1.9026911
    ],
    "remote_derived": false,
    "domain_derived": "aecom.com",
    "description_text": "Company Description\nWork with Us. Change the World.\nAt AECOM, we're delivering a better world. Whether improving your commute, keeping the lights on, providing access to clean water, or transforming skylines, our work helps people and communities thrive. We are the world's trusted infrastructure consulting firm, partnering with clients to solve the world’s most complex challenges and build legacies for future generations.\nThere has never been a better time to be at AECOM. With accelerating infrastructure investment worldwide, our services are in great demand. We invite you to bring your bold ideas and big dreams and become part of a global team of over 50,000 planners, designers, engineers, scientists, digital innovators, program and construction managers and other professionals delivering projects that create a positive and tangible impact around the world.\nWe're one global team driven by our common purpose to deliver a better world. Join us.\nJob Description\nStart here. Grow here. \nOur Lighting Team is seeking a Senior Lighting Engineer to drive the future of lighting across the UK. This role offers an exciting opportunity to influence infrastructure projects from conception through completion.\nEach team member has a development plan to provide a clear pathway to personal development and career progression. The team provides technical leadership of projects throughout the infrastructure lifecycle from feasibility, preliminary and detailed stage designs in some cases through construction.\nOur clients are many and varied from the private and public sector working with numerous local authorities, we work with internal client from transport, rail etc.\nHere’s what you’ll do:\nDevelop: Manage engineering tasks, explore subject areas, define project scopes, and create unique solutions.\nAdvise: Provide expert technical knowledge and support across multi-disciplinary projects.\nDesign: from conceptual stages to implementation which will include site visits, lighting designs, private cable calculation designs, CAD designs, production of lighting specifications, Bills of Quantities and liaison with DNO suppliers.\nEnsure Quality: Strong efficiencies on quality and budget control on projects, navigate the complexities of transportation and landscape projects, working with clients to address and resolve challenges.\nCollaborate: Build strong relationships with technical teams and clients, leading multi-disciplinary efforts to achieve integrated design solutions.\nCome grow with us:\nAnd let's not forget about the perks at AECOM. You'll enjoy a range of core and personalised benefits designed to support your future and well-being, customized to fit your lifestyle. Take advantage of career development opportunities, our flexible hybrid working model to ensure a work-life balance that suits your lifestyle, technical practice networks, AECOM University, and volunteering days. \nQualifications\nReady to push the limits of what’s possible? \nRequirements:\nRelevant Technical Qualifications: Ideally, you possess an ILP Exterior Lighting Diploma or equivalent qualification in a related technical field.\nProven Design Experience: Demonstrated success in a lighting design environment, with a proactive and creative approach to problem-solving.\nSoftware Proficiency: Proficient in industry-standard software, including Lighting Reality, AGi32, Dialux, and Amtech Pro Design to create and assess detailed lighting schemes.\nStrong Communication and Interpersonal Skills: Exceptional written and verbal communication skills, with the ability to confidently and diplomatically engage with staff, colleagues, and clients.\nProject Management: Oversee project timelines, budgets, and resources to ensure projects are delivered on schedule, within budget, and to the highest quality standards. Manage client expectations and project requirements from inception through to completion.\nAdditional Information\nAt AECOM, we value everyone's unique contributions and perspectives. If you meet some of the requirements above or have transferable skills you believe would benefit us, we would be delighted to hear from you!\nInterested in the role or curious about life at AECOM? Follow us on LinkedIn, Facebook, Instagram, and YouTube to explore our AECOM voices, employee stories, latest projects, and much more! \nWorking locations is flexible across the UK (Hybrid - office/remote working), while attendance will be required a nearest local office from time to time (minimum once a week).\nAbout AECOM\nAECOM is the world’s trusted infrastructure consulting firm, delivering professional services throughout the project lifecycle – from advisory, planning, design and engineering to program and construction management. On projects spanning transportation, buildings, water, new energy and the environment, our public- and private-sector clients trust us to solve their most complex challenges. Our teams are driven by a common purpose to deliver a better world through our unrivaled technical and digital expertise, a culture of equity, diversity and inclusion, and a commitment to environmental, social and governance priorities. AECOM is a Fortune 500 firm and its Professional Services business had revenue of $14.4 billion in fiscal year 2023. See how we are delivering sustainable legacies for generations to come at aecom.com and @AECOM.\nFreedom to Grow in a World of Opportunity \nYou will have the flexibility you need to do your best work with hybrid work options. Whether you’re working from an AECOM office, remote location or at a client site, you will be working in a dynamic environment where your integrity, entrepreneurial spirit and pioneering mindset are championed.\nYou will help us foster a safe and respectful workplace, where we invite everyone to bring their whole selves to work using their unique talents, backgrounds and expertise to create transformational outcomes for our clients.\nAECOM provides a wide array of compensation, benefits and well-being programs to meet the diverse needs of our employees and their families. We’re the world’s trusted global infrastructure firm, and we’re in this together – your growth and success are ours too.\nJoin us, and you’ll get all the benefits of being a part of a global, publicly traded firm – access to industry-leading technology and thinking and transformational work with big impact and work flexibility. As an Equal Opportunity Employer, we believe in each person’s potential, and we’ll help you reach yours.\nWe are a Disability Confident Employer and will offer an interview to applicants who have a disability or long-term condition, who meet the minimum/essential criteria for the role. Please let us know using this email address [email protected] if you would like to apply through the Disability Confident Interview Scheme.\nAll your information will be kept confidential according to EEO guidelines."
  },
  {
    "id": "1862281520",
    "date_posted": "2025-09-02T10:53:40.316",
    "date_created": "2025-09-02T10:57:07.616838",
    "title": "RESPONSABLE OPC AÉROPORTUAIRE / INFRASTRUCTURES LINÉAIRES F/H",
    "organization": "Ingérop",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "18 Rue des 2 Gares",
          "addressLocality": "Rueil-Malmaison",
          "addressRegion": "Île-de-France",
          "postalCode": "92500",
          "addressCountry": "France"
        }
      }
    ],
    "locations_alt_raw": [
      "18 Rue des 2 Gares, 92500 Rueil-Malmaison, France"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Temps complet"
    ],
    "url": "https://jobs.smartrecruiters.com/Ingrop/744000079456065-responsable-opc-aeroportuaire-infrastructures-lineaires-f-h",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Rueil-Malmaison"
    ],
    "counties_derived": [
      "Hauts-de-Seine"
    ],
    "regions_derived": [
      "Ile-of-France"
    ],
    "countries_derived": [
      "France"
    ],
    "locations_derived": [
      "Rueil-Malmaison, Ile-of-France, France"
    ],
    "timezones_derived": [
      "Europe/Paris"
    ],
    "lats_derived": [
      48.889884
    ],
    "lngs_derived": [
      2.176286
    ],
    "remote_derived": false,
    "domain_derived": "ingerop.fr",
    "description_text": "Description de l'entreprise\nRejoindre Ingérop, c’est contribuer à façonner le monde de demain.\nGroupe d’ingénierie et de conseil indépendant, nous menons des projets ambitieux dans les domaines du bâtiment, de l’énergie, de l’industrie, de l’eau, des infrastructures, des transports et de la ville.\nAvec plus de 40 sites en France, 98 implantations dans le monde et plus de 3 500 collaborateurs, nous offrons de nombreuses opportunités, en conception comme en réalisation, en local comme à l’international.\nChez Ingérop, vous évoluerez dans un environnement innovant, humain et solidaire, où l’expertise, l’esprit d’équipe et la convivialité sont au cœur de notre culture. Rejoignez une communauté de passionnés !\nDescription du poste\nVous serez rattaché(e) au Siège d’Ingérop situé à Rueil-Malmaison tandis que le lieu de travail quotidien sera basé sur chantier à l'aéroport d'Orly.\nDans le cadre de ses grands projets d'infrastructures et aéroportuaires, le service AMO Infrastructures du pôle Infrastructures recherche son futur Responsable OPC Travaux en CDI.\nLe pôle assure des missions d’OPC et de suivi de travaux plus particulièrement dans le domaine aéroportuaire et d'aménagement de routes ou autoroutes. Les projets aéroportuaires traitent de travaux de refection de pistes, de postes avions, de routes de service, etc. Notre activité porte aussi sur des travaux de routes et autoroutes avec des missions OPC et de suivi de travaux dans le cadre de MOE plus particulièrement.\nLes projets sont situés en région parisienne. Les montants de travaux s’élèvent à plusieurs dizaines de millions d’euros.\nVos missions d'OPC Travaux comprennent :\nLa production et le suivi du planning,\nL'établissement des carnets de phasage,\nLa production des reportings (reporting mensuel, tableaux de suivi, tableaux d'avancement, plans de phasage spatio-temporels, jalons, suivis d'avancement de travaux sur chantier, etc.),\nL'animation des réunions de coordination, \nUne présence permanente sur site avec visite quotidienne, vérification des dispositifs de sécurité, etc.\nVous êtes donc le chef d’orchestre du respect du planning entre les différents lots de travaux et le garant des délais. Vous représentez la mission OPC auprès des différents MOE, titulaires et du Maitre d’ouvrage (MOA) sur votre périmètre.\nQualifications\nDe formation technicien type BTS ou DUT génie civil ou supérieure type école d’ingénieur ou diplôme universitaire bac+5 dans le domaine des travaux publics.\n\nVous êtes jeune diplômé ou vous bénéficiez d’une expérience réussie de 3 à 5 ans dans le domaine de l'OPC ou de la maitrise d’œuvre travaux sur des projets d’envergure similaire.\nVous possédez de solides connaissances des métiers de l'OPC et de maitrise d’œuvre travaux d’opérations d’infrastructures linéaires et/ou aéroportuaires.\nVous êtes autonome dans vos missions et avez l’expérience de l'OPC travaux ou de la MOE travaux (mission DET/AOR de la Loi MOP).\n\nVous êtes reconnu pour vos qualités relationnelles et pour votre sang-froid.\nVous êtes rigoureux, attentif à la sécurité sur le chantier mais aussi exigeant sur la qualité du travail et la protection de l’environnement.\nInformations complémentaires\nVotre package :\nVotre rémunération fixe mensuelle\nUne charte télétravail\nL’acquisition de jours de RTT\nUn Compte Epargne Temps (CET)\nLe droit à des CESU\nL’accès à l’épargne salariale / l’intéressement / la participation\nL’affiliation à une mutuelle et une prévoyance de qualité\nUne politique de formation individualisée et des parcours métiers\nL’accompagnement de votre évolution professionnelle et de vos souhaits de mobilité géographique\nUn CSE dynamique\nIngérop attache de l’importance à la diversité de ses équipes et agit pour l'insertion des personnes en situation de handicap. Nous étudions chaque candidature à compétences égales.\nVotre engagement, notre ambition, ensemble inventons demain !\n#LI-Hybrid #EngineeringJobs #NowHiring #JoinOurTeam #IND/INGEROP"
  },
  {
    "id": "1862281518",
    "date_posted": "2025-09-02T10:53:35.828",
    "date_created": "2025-09-02T10:57:07.357824",
    "title": "PĀRDEVĒJUS-KONSULTANTUS T/C Galerija Riga (nepilna laika)",
    "organization": "H&M Group",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Dzirnavu iela 67",
          "addressLocality": "Rīga",
          "postalCode": "1011",
          "addressCountry": "Latvia"
        }
      }
    ],
    "locations_alt_raw": [
      "Dzirnavu iela 67, Centra rajons, Rīga, LV-1011, Latvija"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Nepilna laika"
    ],
    "url": "https://jobs.smartrecruiters.com/HMGroup/744000079456035-pardevejus-konsultantus-t-c-galerija-riga-nepilna-laika-",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Riga"
    ],
    "counties_derived": null,
    "regions_derived": null,
    "countries_derived": [
      "Latvia"
    ],
    "locations_derived": [
      "Riga, Latvia"
    ],
    "timezones_derived": [
      "Europe/Riga"
    ],
    "lats_derived": [
      56.954311649999994
    ],
    "lngs_derived": [
      24.120623724060515
    ],
    "remote_derived": false,
    "domain_derived": "hmgroup.com",
    "description_text": "Darba apraksts\nKĀDI BŪS TAVI PIENĀKUMI\nKā pārdevējam-konsultantam Tev būs svarīga loma izcilas klientu pieredzes radīšanā. Tu sagaidīsi un sveicināsi mūsu klientus, vadīsi viņus caur veikalu un palīdzēsi atrast vajadzīgo, vienlaikus demonstrējot mūsu sortimentu. Rīkojoties saskaņā ar mūsu vērtībām, Tu veicināsi gan savus, gan uzņēmuma panākumus.\nTu:\nDalīsies ar savām zināšanām par modi un mūsu sortimentu, lai palīdzētu klientiem pieņemt apzinātas izvēles.\nSadarbosies ar savu komandu, lai sniegtu izcilu atbalstu katrā klienta \"ceļojuma\" posmā.\nNodrošināsi, ka tirdzniecības zāle, noliktava un personāla telpas būtu labi aprīkotas, sakārtotas un aicinošas.\nPalīdzēsi veikt veikala atvēršanās un aizvēršanās rutīnas.\nPozitīvi reprezentēsi sevi un mūsu zīmolu, kontaktējoties ar klientiem.\nAR KO TU STRĀDĀSI\nMūsu veikali ir mūsu uzņēmuma sirds, kur klienti iepazīst mūsu zīmolu. Tev kā dinamiskās veikala komandas daļai — no pārdevējiem-konsultantiem, nodaļu vadītājiem, veikalu vadītājiem un vizuālajiem dekoratoriem līdz finanšu operatoram — ir jāpalīdz radīt iedvesmojošu un viesmīlīgu vidi. Tu arī sazināsieties ar plašāko apgabala komandu, sadarbojoties dažādos veikalos, lai dalītos gūtajā pieredzē un kopīgi gūtu panākumus. Kopā ar savu komandu Tev būs svarīga loma, palīdzot klientiem justies pārliecinātiem un izteikt savu individualitāti ar jaunākajām tendencēm un nenovecojošiem stila pamatiem. Veidojot nozīmīgus sakarus ar klientiem mūsu veikalos, mēs padarām modi pieejamu visiem un ilgtspējīgu.\nKAS TU ESI\nMēs meklējam tādus cilvēkus, kuri…\nVēlas palīdzēt klientiem un interesējas par modi vai tirdzniecības procesiem – mēs iemācīsim visu pārējo!\nPieredze klientu apkalpošanā modes, mazumtirdzniecības vai līdzīgās jomās tiks uzskatīta par priekšrocību.\nUn cilvēkus, kuri…​\nPlaukst dinamiskā un uz sadarbību balstītā vidē;\nIr komunikabli, radoši, zinātkāri un ar vēlmi strādāt ar veikalu tehnoloģijām, mācīties un attīstīties;\nIr elastīgi un uz darbībām orientēti.\nKAS MĒS ESAM\nH&M Grupa ir globāls ietekmīgu modes zīmolu uzņēmums. Mūsu mērķis ir pierādīt, ka nevajag meklēt kompromisu starp izcilu dizainu, pieņemamām cenām un ilgtspējīgiem risinājumiem. Mēs vēlamies padarīt modi pieejamu ikvienam, un mūsu klienti ir katra mūsu lēmuma pamatā.\nMūsu uzņēmums sastāv no tūkstošiem degsmīgu un talantīgu kolēģu, kurus vieno mūsu kopīgā kultūra un vērtības. Mēs vēlamies izmantot mūsu kopīgo spēku, mērogu un zināšanas, lai virzītu modes industriju uz iekļaujošāku un ilgtspējīgāku nākotni.\nKĀDĒĻ TEV PATIKS ŠEIT STRĀDĀT \n\nH&M Grupā mēs lepojamies, ka esam tik dinamisks un pretimnākošs uzņēmums. Mēs piedāvājam saviem darbiniekiem pievilcīgus labumus ar plašām attīstības iespējām visā pasaulē.\n25% personāla atlaide visos mūsu H&M Grupas zīmolos – gan veikalos, gan tiešsaistē (H&M, COS, Weekday, Monki, H&M HOME un citi stāsti un ARKET).\nVeselības apdrošināšana pēc pārbaudes laika beigām \nPapildu atlaižu kuponi izmantošanai H&M veikalos ​ \nElastīgs darba grafiku​ \nSociālās garantijas – apmaksāti ikgadējie atvaļinājumi, slimības lapas, utt.\nJOIN US​\nMūsu unikalitāti veido vairāku aspektu kombinācija — mūsu iekļaujošā un uz sadarbību balstītā iekšējā kultūra, mūsu spēcīgās vērtības un izaugsmes iespējas, bet galvenokārt mūsu kolēģi ir tie, kas padara mūs tādus, kādi mēs esam.\nMeklējam pilnas un nepilnas slodzes (20,30h/n) darbiniekus.\nStundas likme 5.84 Eur brutto\nSper nākamo soli savā karjerā kopā ar mums! Ceļojums sākas šeit.\n*Mēs esam apņēmušies nodrošināt godīgu, taisnīgu un uz kompetencēmi balstītu personāla atlases procesu. Tādēļ lūdzam nepievienot pieteikumam motivācijas vēstuli. \nKvalifikācijas\nPapildus informācija"
  },
  {
    "id": "1862281516",
    "date_posted": "2025-09-02T10:53:30.409",
    "date_created": "2025-09-02T10:57:07.250874",
    "title": "STELLVERTRETENDE/R FILIALLEITER/IN (M/W/D) - Traunstein",
    "organization": "JYSK",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Wasserburger Straße",
          "addressLocality": "Traunstein",
          "addressRegion": "Bavaria",
          "postalCode": "83278",
          "addressCountry": "Germany"
        }
      }
    ],
    "locations_alt_raw": [
      "Wasserburger Str., 83278 Traunstein, Deutschland"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Vollzeit"
    ],
    "url": "https://jobs.smartrecruiters.com/JYSK/744000079455658-stellvertretende-r-filialleiter-in-m-w-d-traunstein-",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Traunstein"
    ],
    "counties_derived": [
      "Landkreis Traunstein"
    ],
    "regions_derived": [
      "Bavaria"
    ],
    "countries_derived": [
      "Germany"
    ],
    "locations_derived": [
      "Traunstein, Bavaria, Germany"
    ],
    "timezones_derived": [
      "Europe/Berlin"
    ],
    "lats_derived": [
      47.87756911730472
    ],
    "lngs_derived": [
      12.63759546535734
    ],
    "remote_derived": false,
    "domain_derived": "jysk.com",
    "description_text": "Stellenbeschreibung\nEs macht dir Spaß, deine Kollegen zu motivieren, gemeinsam die besten Ergebnisse zu erreichen? Du willst jeden Tag ein Stückchen besser werden? Du erkennst Möglichkeiten, wo andere Hindernisse sehen, und willst mit deinem Team für das beste Einkaufserlebnis unserer Kunden sorgen?\nDann ist die Stelle als stellvertretender Filialleiter das perfekte Match für dich!\nWAS WIR DIR BIETEN\nJYSK hat es sich als Ziel gesetzt, die erste Wahl der Mitarbeiter im Einzelhandel zu sein. Jetzt hast du die Chance, ein Teil davon zu werden und zusammen mit uns an diesem großen Ziel zu arbeiten!\nJYSK ist ein dynamisches Unternehmen und bei uns wird deine Stimme gehört. Du wirst involviert und deine Entwicklung ist uns sehr wichtig. Um dich in deiner Rolle als stellvertretender Filialleiter bestmöglich zu stärken, bieten wir dir:\nMöglichkeiten für deine eigene Entwicklung durch ausgezeichnetes Training und Mentoring\nFlexible Arbeitszeitgestaltung mit einem arbeitsfreien Samstag im Monat\n20% Mitarbeiterrabatt\nUrlaubs- und Weihnachtsgeld sowie umsatzorientierte Bonuszahlungen\nBetriebliche Altersvorsorge und ein AG-Zuschuss zur Entgeltumwandlung von 30%\nExklusive Mitarbeitervorteile und Zugang zu zahlreichen Corporate Benefits \nSteuerfreies Gehaltsextra mit einer mtl. Sachbezugskarte in Höhe von bis zu 50€\nInterne Wettbewerbe mit attraktiven Prämien sowie Teamevents und unsere Jahresfeier\n36 Tage Urlaub\nWAS BEINHALTET DEINE NÄCHSTE STELLE\nGemeinsam mit der Filialleitung bist du für eine JYSK-Filiale verantwortlich\nEntsprechend der JYSK-Werte unterstützt du deine Filialleitung bei der Weiterentwicklung des Filialteams auf der Verkaufsfläche\nDu ergreifst die Initiative, um Kennzahlen positiv zu beeinflussen und motivierst das Team, großartige Ergebnisse zu erzielen\nDu setzt die Filialkonzepte und -routinen um und hältst diese nach\nDu magst Bewegung und körperliche Arbeit und agierst als Vorbild, indem du zusammen mit der Filialleitung, die Verantwortung im Verkauf und den Routineaufgaben in der Filiale übernimmst\nWAS SOLLTEST DU MITBRINGEN\nFür uns zählt deine Einstellung, alles andere können wir dir beibringen, deswegen sind Quereinsteiger auch herzlich willkommen\nDu bist inspirierend und kommunikativ und schaffst hierdurch eine positive Arbeitsumgebung\nDu strebst immer danach, die besten Ergebnisse zu erzielen\nSelbst in stressigen Situationen bleibst du fokussiert und motivierst dein Team\nDu bist bereit, auch an Samstagen zu arbeiten und hast dafür einen Tag in der Woche frei\nDu brennst für den Verkauf und bist ein kompetenter Kundenberater\nIST DAS DEINE NÄCHSTE CHANCE? Bewirb dich noch heute!\nÜber uns\nWir sind überzeugt, dass unsere Mitarbeiter der Schlüssel zu unserem Erfolg sind. Deshalb setzen wir alles daran, Entwicklungsmöglichkeiten zu bieten und neue Herausforderungen innerhalb von JYSK zu schaffen. Seit unser Gründer, Lars Larsen, 1979 sein erstes Geschäft in Dänemark eröffnet hat, haben wir unsere globale Präsenz mit Filialen und Onlineshops in vielen Ländern weltweit ausgebaut.\nHinweis: In unseren Stellenanzeigen wird aus Gründen der besseren Lesbarkeit die männliche Form der Anrede verwendet. Die weibliche/ diverse Form ist stets mit eingeschlossen, denn Menschen sind vielfältig. Bei JYSK sind alle Menschen unabhängig von ihrem Geschlecht, Alter, Religion, Behinderung, ethnischer Herkunft oder sexueller Identität willkommen\nLies in unseren Datenschutzhinweisen mehr darüber, wie wir Deine Daten verarbeiten."
  },
  {
    "id": "1862281523",
    "date_posted": "2025-09-02T10:53:00.999",
    "date_created": "2025-09-02T10:57:07.857419",
    "title": "Clinical Research Associate / Senior Clinical Research Associate",
    "organization": "PSI CRO",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Munich",
          "addressRegion": "Bavaria",
          "addressCountry": "Germany"
        }
      }
    ],
    "locations_alt_raw": [
      "Munich, Germany"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/PSICRO/744000079455988-clinical-research-associate-senior-clinical-research-associate",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Munich"
    ],
    "counties_derived": null,
    "regions_derived": [
      "Bavaria"
    ],
    "countries_derived": [
      "Germany"
    ],
    "locations_derived": [
      "Munich, Bavaria, Germany"
    ],
    "timezones_derived": [
      "Europe/Berlin"
    ],
    "lats_derived": [
      48.1371079
    ],
    "lngs_derived": [
      11.5753822
    ],
    "remote_derived": false,
    "domain_derived": "psi-cro.com",
    "description_text": "Company Description\nWe are the company that cares – for our staff, for our clients, for our partners and for the quality of the work we do. A dynamic, global, mid-size company founded in 1995, we bring together more than 2,800 driven, dedicated and passionate individuals. We work on the frontline of medical science, changing lives, and bringing new medicines to those who need them.\nJob Description\nAs a Senior / Clinical Research Associate at PSI you will be involved in improving patients' lives while enjoying a variety of monitoring tasks and working on clinical studies in different therapeutic indications, maintaining the highest quality standards in the industry.\nOffice-based in Munich/Planegg or Home-based in Germany\nYou will:\nConduct and report all types of onsite monitoring visits as well as remote visits.\nPerform CRF review, source document verification and query resolution.\nBe responsible for site communication and management.\nBe involved in site identification process.\nAssist in training of less expert CRAs, depending on your level of experience.\nQualifications\nCollege/University degree in Life Sciences or an equivalent combination of education, training & experience.\nIndependent on-site monitoring experience in Germany.\nIndependent experience in all types of monitoring visits in AMG studies, Phases II and/or III.\nExperience in Oncology, Hematology, Infectious / Rare / Gastro-intestinal Diseases is a plus.\nFull working proficiency in German, English and MS Office applications.\nAbility to plan, multitask and work in a dynamic team environment.\nCommunication, collaboration, and problem-solving skills.\nAbility to travel and valid driver’s license.\nAdditional Information\nAs a privately owned mid-size CRO, we are constantly growing, offering plenty of opportunities for personal and professional growth. With no investors to please, our management focuses on company culture and operational delivery over quarter-to-quarter profitability.\nMake the right call and take your career to a whole new level. Join a company that focuses on its people and invests in their professional development and success.\nOur extensive onboarding and mentorship program will prepare you to fulfil your tasks with the highest standards, offering you:\nExcellent and flexible working conditions.\nA unique combination of team collaboration and independent work.\nCompetitive salary and benefits package.\nIf you'd like to hear more about PSI, our organic growth and company culture, and learn more about the studies that we run and our high repeat and referral business rates, please apply for this vacancy."
  },
  {
    "id": "1862281517",
    "date_posted": "2025-09-02T10:52:57.07",
    "date_created": "2025-09-02T10:57:07.306492",
    "title": "Senior Lighting Engineer",
    "organization": "AECOM",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Chesterfield",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "Manchester , United Kingdom"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/AECOM2/744000079455965-senior-lighting-engineer",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Manchester"
    ],
    "counties_derived": [
      "Greater Manchester"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Manchester, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      53.4794892
    ],
    "lngs_derived": [
      -2.2451148
    ],
    "remote_derived": false,
    "domain_derived": "aecom.com",
    "description_text": "Company Description\nWork with Us. Change the World.\nAt AECOM, we're delivering a better world. Whether improving your commute, keeping the lights on, providing access to clean water, or transforming skylines, our work helps people and communities thrive. We are the world's trusted infrastructure consulting firm, partnering with clients to solve the world’s most complex challenges and build legacies for future generations.\nThere has never been a better time to be at AECOM. With accelerating infrastructure investment worldwide, our services are in great demand. We invite you to bring your bold ideas and big dreams and become part of a global team of over 50,000 planners, designers, engineers, scientists, digital innovators, program and construction managers and other professionals delivering projects that create a positive and tangible impact around the world.\nWe're one global team driven by our common purpose to deliver a better world. Join us.\nJob Description\nStart here. Grow here. \nOur Lighting Team is seeking a Senior Lighting Engineer to drive the future of lighting across the UK. This role offers an exciting opportunity to influence infrastructure projects from conception through completion.\nEach team member has a development plan to provide a clear pathway to personal development and career progression. The team provides technical leadership of projects throughout the infrastructure lifecycle from feasibility, preliminary and detailed stage designs in some cases through construction.\nOur clients are many and varied from the private and public sector working with numerous local authorities, we work with internal client from transport, rail etc.\nHere’s what you’ll do:\nDevelop: Manage engineering tasks, explore subject areas, define project scopes, and create unique solutions.\nAdvise: Provide expert technical knowledge and support across multi-disciplinary projects.\nDesign: from conceptual stages to implementation which will include site visits, lighting designs, private cable calculation designs, CAD designs, production of lighting specifications, Bills of Quantities and liaison with DNO suppliers.\nEnsure Quality: Strong efficiencies on quality and budget control on projects, navigate the complexities of transportation and landscape projects, working with clients to address and resolve challenges.\nCollaborate: Build strong relationships with technical teams and clients, leading multi-disciplinary efforts to achieve integrated design solutions.\nCome grow with us:\nAnd let's not forget about the perks at AECOM. You'll enjoy a range of core and personalised benefits designed to support your future and well-being, customized to fit your lifestyle. Take advantage of career development opportunities, our flexible hybrid working model to ensure a work-life balance that suits your lifestyle, technical practice networks, AECOM University, and volunteering days. \nQualifications\nReady to push the limits of what’s possible? \nRequirements:\nRelevant Technical Qualifications: Ideally, you possess an ILP Exterior Lighting Diploma or equivalent qualification in a related technical field.\nProven Design Experience: Demonstrated success in a lighting design environment, with a proactive and creative approach to problem-solving.\nSoftware Proficiency: Proficient in industry-standard software, including Lighting Reality, AGi32, Dialux, and Amtech Pro Design to create and assess detailed lighting schemes.\nStrong Communication and Interpersonal Skills: Exceptional written and verbal communication skills, with the ability to confidently and diplomatically engage with staff, colleagues, and clients.\nProject Management: Oversee project timelines, budgets, and resources to ensure projects are delivered on schedule, within budget, and to the highest quality standards. Manage client expectations and project requirements from inception through to completion.\nAdditional Information\nAt AECOM, we value everyone's unique contributions and perspectives. If you meet some of the requirements above or have transferable skills you believe would benefit us, we would be delighted to hear from you!\nInterested in the role or curious about life at AECOM? Follow us on LinkedIn, Facebook, Instagram, and YouTube to explore our AECOM voices, employee stories, latest projects, and much more! \nWorking locations is flexible across the UK (Hybrid - office/remote working), while attendance will be required a nearest local office from time to time (minimum once a week).\nAbout AECOM\nAECOM is the world’s trusted infrastructure consulting firm, delivering professional services throughout the project lifecycle – from advisory, planning, design and engineering to program and construction management. On projects spanning transportation, buildings, water, new energy and the environment, our public- and private-sector clients trust us to solve their most complex challenges. Our teams are driven by a common purpose to deliver a better world through our unrivaled technical and digital expertise, a culture of equity, diversity and inclusion, and a commitment to environmental, social and governance priorities. AECOM is a Fortune 500 firm and its Professional Services business had revenue of $14.4 billion in fiscal year 2023. See how we are delivering sustainable legacies for generations to come at aecom.com and @AECOM.\nFreedom to Grow in a World of Opportunity \nYou will have the flexibility you need to do your best work with hybrid work options. Whether you’re working from an AECOM office, remote location or at a client site, you will be working in a dynamic environment where your integrity, entrepreneurial spirit and pioneering mindset are championed.\nYou will help us foster a safe and respectful workplace, where we invite everyone to bring their whole selves to work using their unique talents, backgrounds and expertise to create transformational outcomes for our clients.\nAECOM provides a wide array of compensation, benefits and well-being programs to meet the diverse needs of our employees and their families. We’re the world’s trusted global infrastructure firm, and we’re in this together – your growth and success are ours too.\nJoin us, and you’ll get all the benefits of being a part of a global, publicly traded firm – access to industry-leading technology and thinking and transformational work with big impact and work flexibility. As an Equal Opportunity Employer, we believe in each person’s potential, and we’ll help you reach yours.\nWe are a Disability Confident Employer and will offer an interview to applicants who have a disability or long-term condition, who meet the minimum/essential criteria for the role. Please let us know using this email address [email protected] if you would like to apply through the Disability Confident Interview Scheme.\nAll your information will be kept confidential according to EEO guidelines."
  },
  {
    "id": "1862281521",
    "date_posted": "2025-09-02T10:52:39.153",
    "date_created": "2025-09-02T10:57:07.687364",
    "title": "Accounts Payable Assistant",
    "organization": "Kanadevia Inova",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Ascent 4, Farnborough Aerospace Centre,",
          "addressLocality": "Farnborough",
          "addressRegion": "Hampshire",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "Ascent 4, Farnborough Aerospace Centre,, Farnborough, Hampshire, United Kingdom"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/KanadeviaInova/744000079455934-accounts-payable-assistant",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Farnborough"
    ],
    "counties_derived": [
      "Hampshire"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Farnborough, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      51.290705
    ],
    "lngs_derived": [
      -0.758031
    ],
    "remote_derived": false,
    "domain_derived": "kanadevia-inova.com",
    "description_text": "Company Description\nWelcome to Kanadevia Inova, a global innovation leader in the waste infrastructure space, where we believe in creating a sustainable future through technology and innovation.\n\nTransforming Waste into Value\n\nAt Kanadevia Inova, we pride ourselves on being at the forefront of waste-to-X technology. We are not just waste managers; we are creators of value from what communities discard. Your role at Kanadevia Inova directly contributes to turning something once considered useless - waste - into something invaluable: energy, heat, hydrogen, fertilizer, and beyond..\n\nFind out more about Kanadevia Inova at www.kanadevia-inova.com.\nJob Description\nWe are currently seeking an experienced, hands-on Accounts Payable Assistant to join our finance team based in Farnborough, Hampshire.\nThis is a great opportunity to work in a collaborative environment and a broad range of transactional finance responsibilities.\nWe do need Accounts Payable experience from mid level and unfortunately this is not an entry-level opportunity and we are not able to provide training for this position.\nThe position is offered on an 18 month fixed term employee basis, with smart working (home/office) available (2 days from home/ 3 days in the office).\nKey Responsibilities:\nAccounts Payable:\nProcessing supplier invoices, including sending for approval via ELO\nEntering approved invoices into SAP B1 / Mari\nProcessing Customer Invoices\nBank Reconciliations\nProcessing Expenses\nProcessing Payments on HSBC & SAP B1 and sending remittances\nCredit Control:\nSending Statements\nCalling customers for payment\nQualifications\nQualifications: \nAAT qualified or studying \nProven track record in a similar accounts role\nGood working knowledge of Excel and financial software\nExcellent communication and interpersonal skills\nSkills & Attributes:\nHighly organised and able to manage competing priorities\nStrong attention to detail\nAble to work across multiple functions and with cross-functional teams\nA flexible, can-do attitude and willingness to support where needed\nAdditional Information\nAnnual salary review and bonus awards\nPension scheme up to 10% employer contribution\nLife insurance 4x Salary\nDisability insurance\nPrivate medical and dental insurance\nFor HR agencies: Please note that we do not accept applications coming from agencies. Thank you."
  },
  {
    "id": "1862281522",
    "date_posted": "2025-09-02T10:52:30.724",
    "date_created": "2025-09-02T10:57:07.77605",
    "title": "CHEF DE PROJET ÉLECTRICITÉ - CFO / COURANTS FORTS F/H",
    "organization": "Ingérop",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Rue des 2 Gares 18",
          "addressLocality": "Rueil-Malmaison",
          "addressRegion": "Île-de-France",
          "postalCode": "92500",
          "addressCountry": "France"
        }
      }
    ],
    "locations_alt_raw": [
      "18 Rue des 2 Gares, 92500 Rueil-Malmaison, France"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Temps complet"
    ],
    "url": "https://jobs.smartrecruiters.com/Ingrop/744000079455905-chef-de-projet-electricite-cfo-courants-forts-f-h",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Rueil-Malmaison"
    ],
    "counties_derived": [
      "Hauts-de-Seine"
    ],
    "regions_derived": [
      "Ile-of-France"
    ],
    "countries_derived": [
      "France"
    ],
    "locations_derived": [
      "Rueil-Malmaison, Ile-of-France, France"
    ],
    "timezones_derived": [
      "Europe/Paris"
    ],
    "lats_derived": [
      48.889884
    ],
    "lngs_derived": [
      2.176286
    ],
    "remote_derived": false,
    "domain_derived": "ingerop.fr",
    "description_text": "Description de l'entreprise\nRejoindre Ingérop, c’est contribuer à façonner le monde de demain.\nGroupe d’ingénierie et de conseil indépendant, nous menons des projets ambitieux dans les domaines du bâtiment, de l’énergie, de l’industrie, de l’eau, des infrastructures, des transports et de la ville.\nAvec plus de 40 sites en France, 98 implantations dans le monde et plus de 3 500 collaborateurs, nous offrons de nombreuses opportunités, en conception comme en réalisation, en local comme à l’international.\nChez Ingérop, vous évoluerez dans un environnement innovant, humain et solidaire, où l’expertise, l’esprit d’équipe et la convivialité sont au cœur de notre culture. Rejoignez une communauté de passionnés !\nDescription du poste\nVous serez rattaché(e) au Siège d’Ingérop situé à Rueil-Malmaison. Des déplacements hebdomadaires sont à prévoir au niveau national.\nVous avez développé des compétences en HTB et vous souhaitez les valoriser, rejoignez-nous en CDI pour un nouveau challenge ! Nous recherchons justement un Chef de projet Electricité – Courants Forts (CFO), dans le cadre du développement du service sur la partie HTB.\nVous serez rattaché au service Activité Systèmes, regroupant plus d’une vingtaine de collaboratrices et collaborateurs. Vous serez accueilli par une équipe pluridisciplinaire et dynamique, animée par le chef de service.\nEn tant que Chef de projet chez Ingérop, votre quotidien sera rythmé par des missions techniques et pas que…\nPour commencer :\nNous vous confierons les missions dans le domaine des Courants Forts (CFO) : installations électriques Haute Tension HTA et HTB, Basse Tension (HTBT), éclairage public et éclairage tunnels,…:\nEtudes : Diagnostic, Etudes Préliminaires (EP), Avant-Projet (AVP), Projet (PRO), Assistance à la passation des contrats de travaux (ACT),\nTravaux : VISA et Etudes d’exécution (EXE), suivis des travaux (DET) et assistance aux opérations de réception (AOR).\nMais aussi :\nVous serez amené à développer la partie HTB chez les clients RTE, Enedis,…\nVous serez associé à la réalisation d’offres commerciales et techniques dans les domaines HTA et HTB,\nPossibilités d’évolution\nChez Ingérop et en fonction de vos appétences, vos compétences techniques ainsi que vos qualités de conduite de projet, de développement commercial et entrepreneuriales vous permettent d'évoluer vers un poste d’Adjoint Chef de service ou de Chef de service.\nQualifications\nDe formation ingénieur, Master II ou Bac+5 (CentraleSupélec, IMPGT, IMT, HEI, etc) dans le domaine électricité.\nVous justifiez de 5 à 10 ans d’expérience dont 2 ans d’expérience minimum comme chef de projet spécifiquement en CFO et impérativement en HTB.\nVous maîtrisez les référentiels techniques ENEDIS et RTE.\nLa maîtrise de l’outil CANECO sera quant à elle appréciée.\nVous êtes organisé, autonome, curieux, doté d’agilité dans la communication tant orale qu’écrite.\nInformations complémentaires\nVotre package :\nVotre rémunération fixe mensuelle\nUne charte télétravail\nL’acquisition de jours de RTT\nUn Compte Epargne Temps (CET)\nLe droit à des CESU\nL’accès à l’épargne salariale / l’intéressement / la participation\nL’affiliation à une mutuelle et une prévoyance de qualité\nUne politique de formation individualisée et des parcours métiers\nL’accompagnement de votre évolution professionnelle et de vos souhaits de mobilité géographique\nUn CSE dynamique\nVous avez envie de participer à une aventure riche en projets d'envergure/intéressants ? D’avoir des challenges collaboratifs ? De vous retrouver lors de moments conviviaux ?\nIngérop attache de l’importance à la diversité de ses équipes et agit pour l'insertion des personnes en situation de handicap. Nous étudions chaque candidature à compétences égales.\nVotre engagement, notre ambition, ensemble inventons demain !\n#LI-Hybrid #EngineeringJobs #NowHiring #JoinOurTeam #IND/INGEROP"
  },
  {
    "id": "1862281526",
    "date_posted": "2025-09-02T10:52:27.391",
    "date_created": "2025-09-02T10:57:09.900484",
    "title": "Buying Assistant Kids",
    "organization": "wehkamp",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Zwolle",
          "addressRegion": "Overijssel",
          "addressCountry": "Netherlands"
        }
      }
    ],
    "locations_alt_raw": [
      "Zwolle, Nederland"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Voltijds"
    ],
    "url": "https://jobs.smartrecruiters.com/wehkamp/744000079455875-buying-assistant-kids",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Zwolle"
    ],
    "counties_derived": null,
    "regions_derived": [
      "Overijssel"
    ],
    "countries_derived": [
      "Netherlands"
    ],
    "locations_derived": [
      "Zwolle, Overijssel, Netherlands"
    ],
    "timezones_derived": [
      "Europe/Amsterdam"
    ],
    "lats_derived": [
      52.5089759
    ],
    "lngs_derived": [
      6.0943765
    ],
    "remote_derived": false,
    "domain_derived": "wehkamp.nl",
    "description_text": "Functieomschrijving\nAls Buying Assistant ben jij de drijvende kracht achter onze Kids categorie!\nJe zorgt ervoor dat inkooporders vlekkeloos worden verwerkt, ondersteunt bij creatieve marketinguitingen en bent de rechterhand van de inkoper. Dankzij jouw inzet verschijnen onze producten razendsnel en tiptop op de site – uiteraard in nauwe samenwerking met onze fotostudio.\nMaar je doet meer dan alleen ondersteunen: jij denkt mee, signaleert verbeterkansen en draagt actief bij aan het optimaliseren van processen en klantbeleving. Zo maak jij elke dag het verschil.\nBen jij iemand die energie krijgt van een dynamische werkomgeving, graag de touwtjes in handen neemt en samen met je team successen viert? Dan is deze rol als Buying Assistant jou op het lijf geschreven!\nFunctie-eisen\nJe hebt een afgeronde commerciële opleiding en bent helemaal thuis in de wereld van trends. Of het nu gaat om Fashion of social media: jij volgt alles op de voet en weet precies wat er speelt.\nDaarnaast ben je nauwkeurig, cijfermatig en analytisch sterk. Je beheerst zowel Nederlands als Engels uitstekend, zodat je moeiteloos schakelt met onze nationale én internationale leveranciers.\nWij zijn ambitieus, en dat verwachten we ook van jou. Dynamiek klinkt jou als muziek in de oren en een volle to-do-lijst zie jij niet als last, maar als een uitdaging. Ondernemerschap zit in jouw DNA: je hebt oog voor de details die in retail écht het verschil maken, je ontzorgt je collega’s en komt met frisse, toffe ideeën.\nAanvullende informatie\nWij helpen jou elke dag om alles uit jouw carrière te halen. Jouw ontwikkeling en jouw persoonlijke groei zijn een wederzijdse commitment: Wehkamp Retail Group groeit, jij groeit. Jij groeit, Wehkamp Retail Group groeit.\nVerder bieden we:\nSalaris passend bij jouw ervaring;\nVakantietoeslag van 10,5%;\n25 vakantiedagen;\nWinstdeling;\nFietslease en fietsplan;\nMogelijkheid om te sporten in onze eigen sportschool;\nReiskostenvergoeding én een thuiswerkvergoeding;\nGoede pensioenregeling;\nElk jaar de mogelijkheid om te groeien binnen jouw salarisschaal;\nKorting op jouw aanvullende zorgverzekering;\nPersoneelskorting op nagenoeg het gehele assortiment van Wehkamp.nl"
  },
  {
    "id": "1862281265",
    "date_posted": "2025-09-02T10:52:26.27",
    "date_created": "2025-09-02T10:52:26.418693",
    "title": "Part-time Nursing Laboratory Officer (N&HS)",
    "organization": "Hong Kong Metropolitan University",
    "organization_url": null,
    "date_validthrough": "2025-09-21T23:59:00",
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "",
          "addressLocality": "Hong Kong"
        }
      }
    ],
    "locations_alt_raw": null,
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": null,
    "url": "https://hkmu.taleo.net/careersection/ex_non_full_time/jobdetail.ftl?job=25001VS&lang=en",
    "source_type": "ats",
    "source": "taleo",
    "source_domain": "hkmu.taleo.net",
    "organization_logo": null,
    "cities_derived": null,
    "counties_derived": null,
    "regions_derived": [
      "Hong Kong"
    ],
    "countries_derived": [
      "China"
    ],
    "locations_derived": [
      "Hong Kong, China"
    ],
    "timezones_derived": [
      "Asia/Hong_Kong"
    ],
    "lats_derived": [
      22.350627
    ],
    "lngs_derived": [
      114.1849161
    ],
    "remote_derived": false,
    "domain_derived": "hkmu.edu.hk",
    "description_text": "Founded in 1989, Hong Kong Metropolitan University (HKMU) is a modern, vibrant and dynamic university. We tailor our professional programmes to adapt to market trends and meet industry needs, thus providing our students with quality professional education and clear career paths. Being the first University of Applied Sciences (UAS) in Hong Kong, we pledge to play a pioneering role in enhancing recognition of vocational and professional education and training, and nurturing talents with both applied skills and knowledge.\nAs a faculty-driven, student-centred university in support of innovative teaching and learning, strategic research, and stakeholder outreach to provide maximum benefit to our communities, we conduct research that advances knowledge and enhances teaching, focusing on strategic areas, including digital humanities and literature, international business, gerontechnology, personalised care, smart city, open and innovative education, and bilingual learning and teaching.\nHKMU is becoming an ever more vital link in addressing and helping Hong Kong to solve many difficult challenges – as part of our involvement in, and commitment to, the ‘metropolis’ of Hong Kong. Our plans to expand into the Greater Bay Area (GBA) will also cultivate talent to serve Hong Kong and the wider metropolitan GBA.\nFor more information about the University, please visit https://www.hkmu.edu.hk.\nThe School of Nursing and Health Sciences offers a number of programmes in Nursing and Health Sciences at Diploma, Higher Diploma, Bachelor and Master levels.\nWe are now looking for a suitable person to fill the following position in the School of Nursing and Health Sciences:\n\n\nMajor Duties and Responsibilities\nThe appointee will be responsible mainly for the following:\nassisting in the preparation of necessary materials and equipment for tutorial classes;\nensuring smooth operation and maintaining laboratory safety in the Clinical Nursing Education Centre;\nassisting with equipment and materials management, as well as clearing the laboratory after tutorial classes;\nproviding support for final year projects;\nensuring that laboratories, materials and equipment are kept clean; tidy and in good order;\nsupervising and instructing students on the correct use of equipment and materials as well as promoting good laboratory practice;\nwith the possibility of working irregular hours when required; and\nundertaking any other duties and responsibilities as assigned. \nCandidates\nCandidates should possess the following qualifications, experience and competence:\na recognized degree in Nursing or a related health discipline;\ngood communication, interpersonal and organisational skills;\na strong sense of responsibility; and\npreferably a qualified first aider.\nRemuneration\nHK$250 per hour\nDuration of Appointment\nWorking hours per week will not be more than 17 hours. 6 hours per week on average for the period from October 2025 to August 2026.\nTerms and Conditions for Appointment\nSuccessful candidates will be appointed on a temporary part-time contract. Benefits will be provided in accordance with the statutory provisions. \nTo Apply\nCandidates who are interested in joining us may submit their applications via the University’s eRecruitment System.\nThe personal data collected will be used for the purpose of considering your application for employment. For details, please refer to the “Personal Data (Privacy) Notice for Job Applicant” on the University’s website. If you are not contacted by the University within eight weeks from the closing date of application, you may assume that your application was unsuccessful."
  },
  {
    "id": "1862281524",
    "date_posted": "2025-09-02T10:52:23.676",
    "date_created": "2025-09-02T10:57:09.68429",
    "title": "Conference & Events Intern",
    "organization": "AccorHotel",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Barcelona",
          "addressRegion": "Catalunya",
          "addressCountry": "Spain"
        }
      }
    ],
    "locations_alt_raw": [
      "Barcelona, Spain"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/AccorHotel/744000079455815-conference-events-intern-",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Barcelona"
    ],
    "counties_derived": [
      "Barcelona"
    ],
    "regions_derived": [
      "Catalonia"
    ],
    "countries_derived": [
      "Spain"
    ],
    "locations_derived": [
      "Barcelona, Catalonia, Spain"
    ],
    "timezones_derived": [
      "Europe/Madrid"
    ],
    "lats_derived": [
      41.3828939
    ],
    "lngs_derived": [
      2.1774322
    ],
    "remote_derived": false,
    "domain_derived": "accor.com",
    "description_text": "Company Description\nSLS Barcelona, a five-star urban resort of extraordinary experiences, brings a new variety of seaside glamour, indulgence and excellence to Barcelona’s waterfront district of Port Forum. Here the hallmarks of an SLS wonderland – playful ambiance, VIP treatment, and theatrical experiences - meet idyllic views to set a lavish stage for the extraordinary to unfold. The only 5-star hotel in the city to feature a terrace off every guestroom (471 in total), SLS Barcelona is all-encompassing in its delight, offering an array of exclusive amenities including rooftop dining and bars, three inviting swimming pools, a spacious 800 square-meter ballroom with abundant natural light, break out rooms catering to all size of meetings, a rejuvenating spa, and a state-of-the-art fitness centre. Say farewell to the ordinary, and hello to the extraordinary! \nJob Description\nWhat you’ll do \nWe are looking for a Groups & Events Intern to join the pre-opening team at SLS Barcelona. Under the guidance of the Conference Director, you will be responsible for planning, coordinating, and executing all conferences and events hosted at SLS Barcelona. \nCollaborate with clients to understand their conference needs, including objectives, budget, and specific requirements. \nDevelop detailed conference event plans, timelines, and schedules to ensure their smooth execution. \nCollaborate to develop and execute promotional strategies to attract clients and maximize event bookings. \nConduct post-event evaluations to assess success, gather client feedback, and identify areas for improvement. \nMaintain high standards of service quality and guest satisfaction, addressing any issues or concerns promptly and effectively. \nQualifications\nWhat we are looking for... \nAbility to multitask, work in a fast-paced environment and have a high-level attention to detail \nExcellent verbal and written communication skills. Fluent in Spanish and English. \nYou make people feel good - your team, guests, and colleagues alike. You make a positive impact. \nInnovative and insightful. \nYou are an excellent relationship builder, confident in working with other teams and leaders; you’re passionate about what we can achieve together. \nYou take ownership of important issues, solve problems, and make effective decisions. \nYou learn quickly and adapt to SLS’s unique culture. \nYou are humble and open to ideas. We leave our ego at the door and help get things done. \nYou’re up for doing things differently and trying (almost) everything once. \nYou want to be part of a team that works hard, supports each other, and has fun along the way. \nAdditional Information\nWhat's in it for you... \nThe opportunity to be part of an innovative, fast-growing, international group that’s committed to not just building new hotels but building a global brand. \nThe chance to challenge the norm and work in an environment that is both creative and rewarding. \nBecome part of a team that’s very passionate about creating great hospitality experiences."
  },
  {
    "id": "1862281528",
    "date_posted": "2025-09-02T10:52:14.281",
    "date_created": "2025-09-02T10:57:10.07281",
    "title": "Specjalista Laboratoryjny (Obsługa Klienta – Fizykochemia)",
    "organization": "Eurofins",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Katowice",
          "addressRegion": "Silesian Voivodeship",
          "addressCountry": "Poland"
        }
      }
    ],
    "locations_alt_raw": [
      "Katowice, Polska"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Pełny etat"
    ],
    "url": "https://jobs.smartrecruiters.com/Eurofins/744000079455765-specjalista-laboratoryjny-obs-uga-klienta-fizykochemia-",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Katowice"
    ],
    "counties_derived": null,
    "regions_derived": [
      "Silesian Voivodeship"
    ],
    "countries_derived": [
      "Poland"
    ],
    "locations_derived": [
      "Katowice, Silesian Voivodeship, Poland"
    ],
    "timezones_derived": [
      "Europe/Warsaw"
    ],
    "lats_derived": [
      50.2598987
    ],
    "lngs_derived": [
      19.0215852
    ],
    "remote_derived": false,
    "domain_derived": "eurofins.com",
    "description_text": "Opis firmy\nEurofins Scientific to międzynarodowa firma, która oferuje wszechstronną gamę badań analitycznych klientom różnych sektorów. Grupa Eurofins jest światowym liderem w badaniach żywności, środowiska, produktów farmaceutycznych, kosmetyków oraz testów agrochemicznych (CRO). Jest także jedną z wiodących na świecie firm na rynkach genomiki, farmakologii, medycyny sądowej, CDMO, zaawansowanych nauk o materiałach oraz badań klinicznych. Ponadto Eurofins silnie rozwija dział diagnostyki klinicznej.\nW 2023 r. Eurofins osiągnęło przychód na poziomie 6.5 mld euro, zatrudniając około 62 000 pracowników w ponad 900 laboratoriach w 62 krajach.\nOpis stanowiska\nWspółpraca z klientem, w zakresie przeglądu zlecenia, potwierdzania wymagań klienta, przekazywania raportów analitycznych z badań,\nDoradztwo z zakresu wykonywanych analiz i interpretacji wyników badań fizykochemicznych nad żywnością,\nGenerowanie i zatwierdzanie raportów analitycznych,\nUczestniczenie w rozpatrywaniu skarg i reklamacji,\nUczestniczenie w audytach wewnętrznych/zewnętrznych,\nPrzestrzeganie zasad normy PN-EN ISO 17025:2018 oraz systemu zarządzania obowiązującego w Eurofins Polska i jego doskonalenie w zakresie swoich odpowiedzialności.\nKwalifikacje\nMin. dwuletnie doświadczenie w pracy w laboratorium na stanowisku laboranta/technika/asystenta lub w wewnętrznym dziale obsługi klienta laboratoryjnego,\nWykształcenie wyższe kierunkowe (technologia żywności, technologia chemiczna, chemia, biotechnologia, ochrona środowiska),\nZnajomość języka angielskiego na poziomie komunikatywnym (B2),\nDobra znajomość pakietu Microsoft Office (Outlook, Excel, Word),\nWysoki poziom komunikatywności,\nDobra organizacja pracy, umiejętność priorytetyzacji zadań,\nUmiejętność pracy w zespole,\nUmiejętność pracy pod presją czasu,\nMile widziane:\nznajomość normy PN-EN ISO 17025:2018,\ndoświadczenie w pracy z systemem LIMS (Laboratory Information Management Systems) i CRM (Customer Relations Management).\nDodatkowe informacje\nZatrudnienie w oparciu o umowę o pracę (trzymiesięczny okres próbny z intencją przedłużenia współpracy na kolejny rok),\nPraca zdalna lub hybrydowa w jednym z naszych oddziałów (Katowice, Łódź lub Malbork),\nElastyczny czas pracy (możliwość rozpoczęcia pracy w przedziale 7:00-9:00),\nPo odbyciu okresu próbnego – możliwość pracy zdalnej,\nDofinansowanie do karty multisport,\nDostęp do prywatnej opieki medycznej w Lux Med,\nPremia stażowa – 500 złotych brutto na każdą rocznicę pracy,\nDofinansowania z Zakładowego Funduszu Świadczeń Socjalnych,\nMożliwość rozwoju – szkolenia specjalistyczne, jasna i klarowna ścieżka kariery,\nPraca w międzynarodowym środowisku,\nPrzyjazna atmosfera pracy w zgranym zespole."
  },
  {
    "id": "1862281297",
    "date_posted": "2025-09-02T10:51:00.569",
    "date_created": "2025-09-02T10:53:04.943481",
    "title": "Senior Lighting Engineer",
    "organization": "AECOM",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Chesterfield",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "Leeds, United Kingdom"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/AECOM2/744000079455177-senior-lighting-engineer",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Leeds"
    ],
    "counties_derived": [
      "West Yorkshire"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Leeds, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      53.7974185
    ],
    "lngs_derived": [
      -1.5437941
    ],
    "remote_derived": false,
    "domain_derived": "aecom.com",
    "description_text": "Company Description\nWork with Us. Change the World.\nAt AECOM, we're delivering a better world. Whether improving your commute, keeping the lights on, providing access to clean water, or transforming skylines, our work helps people and communities thrive. We are the world's trusted infrastructure consulting firm, partnering with clients to solve the world’s most complex challenges and build legacies for future generations.\nThere has never been a better time to be at AECOM. With accelerating infrastructure investment worldwide, our services are in great demand. We invite you to bring your bold ideas and big dreams and become part of a global team of over 50,000 planners, designers, engineers, scientists, digital innovators, program and construction managers and other professionals delivering projects that create a positive and tangible impact around the world.\nWe're one global team driven by our common purpose to deliver a better world. Join us.\nJob Description\nStart here. Grow here. \nOur Lighting Team is seeking a Senior Lighting Engineer to drive the future of lighting across the UK. This role offers an exciting opportunity to influence infrastructure projects from conception through completion.\nEach team member has a development plan to provide a clear pathway to personal development and career progression. The team provides technical leadership of projects throughout the infrastructure lifecycle from feasibility, preliminary and detailed stage designs in some cases through construction.\nOur clients are many and varied from the private and public sector working with numerous local authorities, we work with internal client from transport, rail etc.\nHere’s what you’ll do:\nDevelop: Manage engineering tasks, explore subject areas, define project scopes, and create unique solutions.\nAdvise: Provide expert technical knowledge and support across multi-disciplinary projects.\nDesign: from conceptual stages to implementation which will include site visits, lighting designs, private cable calculation designs, CAD designs, production of lighting specifications, Bills of Quantities and liaison with DNO suppliers.\nEnsure Quality: Strong efficiencies on quality and budget control on projects, navigate the complexities of transportation and landscape projects, working with clients to address and resolve challenges.\nCollaborate: Build strong relationships with technical teams and clients, leading multi-disciplinary efforts to achieve integrated design solutions.\nCome grow with us:\nAnd let's not forget about the perks at AECOM. You'll enjoy a range of core and personalised benefits designed to support your future and well-being, customized to fit your lifestyle. Take advantage of career development opportunities, our flexible hybrid working model to ensure a work-life balance that suits your lifestyle, technical practice networks, AECOM University, and volunteering days. \nQualifications\nReady to push the limits of what’s possible? \nRequirements:\nRelevant Technical Qualifications: Ideally, you possess an ILP Exterior Lighting Diploma or equivalent qualification in a related technical field.\nProven Design Experience: Demonstrated success in a lighting design environment, with a proactive and creative approach to problem-solving.\nSoftware Proficiency: Proficient in industry-standard software, including Lighting Reality, AGi32, Dialux, and Amtech Pro Design to create and assess detailed lighting schemes.\nStrong Communication and Interpersonal Skills: Exceptional written and verbal communication skills, with the ability to confidently and diplomatically engage with staff, colleagues, and clients.\nProject Management: Oversee project timelines, budgets, and resources to ensure projects are delivered on schedule, within budget, and to the highest quality standards. Manage client expectations and project requirements from inception through to completion.\nAdditional Information\nAt AECOM, we value everyone's unique contributions and perspectives. If you meet some of the requirements above or have transferable skills you believe would benefit us, we would be delighted to hear from you!\nInterested in the role or curious about life at AECOM? Follow us on LinkedIn, Facebook, Instagram, and YouTube to explore our AECOM voices, employee stories, latest projects, and much more! \nWorking locations is flexible across the UK (Hybrid - office/remote working), while attendance will be required a nearest local office from time to time (minimum once a week).\nAbout AECOM\nAECOM is the world’s trusted infrastructure consulting firm, delivering professional services throughout the project lifecycle – from advisory, planning, design and engineering to program and construction management. On projects spanning transportation, buildings, water, new energy and the environment, our public- and private-sector clients trust us to solve their most complex challenges. Our teams are driven by a common purpose to deliver a better world through our unrivaled technical and digital expertise, a culture of equity, diversity and inclusion, and a commitment to environmental, social and governance priorities. AECOM is a Fortune 500 firm and its Professional Services business had revenue of $14.4 billion in fiscal year 2023. See how we are delivering sustainable legacies for generations to come at aecom.com and @AECOM.\nFreedom to Grow in a World of Opportunity \nYou will have the flexibility you need to do your best work with hybrid work options. Whether you’re working from an AECOM office, remote location or at a client site, you will be working in a dynamic environment where your integrity, entrepreneurial spirit and pioneering mindset are championed.\nYou will help us foster a safe and respectful workplace, where we invite everyone to bring their whole selves to work using their unique talents, backgrounds and expertise to create transformational outcomes for our clients.\nAECOM provides a wide array of compensation, benefits and well-being programs to meet the diverse needs of our employees and their families. We’re the world’s trusted global infrastructure firm, and we’re in this together – your growth and success are ours too.\nJoin us, and you’ll get all the benefits of being a part of a global, publicly traded firm – access to industry-leading technology and thinking and transformational work with big impact and work flexibility. As an Equal Opportunity Employer, we believe in each person’s potential, and we’ll help you reach yours.\nWe are a Disability Confident Employer and will offer an interview to applicants who have a disability or long-term condition, who meet the minimum/essential criteria for the role. Please let us know using this email address [email protected] if you would like to apply through the Disability Confident Interview Scheme.\nAll your information will be kept confidential according to EEO guidelines."
  },
  {
    "id": "1862281296",
    "date_posted": "2025-09-02T10:50:51.997",
    "date_created": "2025-09-02T10:53:04.887583",
    "title": "CHEF DE PROJET SYSTÈMES ÉLECTRIQUES - CFO/CFA F/H",
    "organization": "Ingérop",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Rue des 2 Gares 18",
          "addressLocality": "Rueil-Malmaison",
          "addressRegion": "Île-de-France",
          "postalCode": "92500",
          "addressCountry": "France"
        }
      }
    ],
    "locations_alt_raw": [
      "18 Rue des 2 Gares, 92500 Rueil-Malmaison, France"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Temps complet"
    ],
    "url": "https://jobs.smartrecruiters.com/Ingrop/744000079454750-chef-de-projet-systemes-electriques-cfo-cfa-f-h",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Rueil-Malmaison"
    ],
    "counties_derived": [
      "Hauts-de-Seine"
    ],
    "regions_derived": [
      "Ile-of-France"
    ],
    "countries_derived": [
      "France"
    ],
    "locations_derived": [
      "Rueil-Malmaison, Ile-of-France, France"
    ],
    "timezones_derived": [
      "Europe/Paris"
    ],
    "lats_derived": [
      48.889884
    ],
    "lngs_derived": [
      2.176286
    ],
    "remote_derived": false,
    "domain_derived": "ingerop.fr",
    "description_text": "Description de l'entreprise\nRejoindre Ingérop, c’est contribuer à façonner le monde de demain.\nGroupe d’ingénierie et de conseil indépendant, nous menons des projets ambitieux dans les domaines du bâtiment, de l’énergie, de l’industrie, de l’eau, des infrastructures, des transports et de la ville.\nAvec plus de 40 sites en France, 98 implantations dans le monde et plus de 3 500 collaborateurs, nous offrons de nombreuses opportunités, en conception comme en réalisation, en local comme à l’international.\nChez Ingérop, vous évoluerez dans un environnement innovant, humain et solidaire, où l’expertise, l’esprit d’équipe et la convivialité sont au cœur de notre culture. Rejoignez une communauté de passionnés !\nDescription du poste\nVous serez rattaché(e) au Siège d’Ingérop situé à Rueil-Malmaison.\nVous avez développé des compétences en CFO et CFA et vous souhaitez les valoriser, rejoignez-nous en CDI pour un nouveau challenge ! Nous recherchons justement un Chef(fe) de projet systèmes électriques Courants Forts (CFO) Courants Faibles (CFA), dans le cadre du développement du service sur la partie CFO CFA.\nVous serez rattaché au service Activité Systèmes, regroupant plus d’une vingtaine de collaboratrices et collaborateurs. Vous serez accueilli par une équipe pluridisciplinaire et dynamique, animée par le chef de service.\nEn tant que Chef(fe) de projet chez Ingérop, votre quotidien sera rythmé par des missions techniques et pas que…\nPour commencer :\nNous vous confierons les missions dans le domaine des Courants Forts (CFO) et Courants Faibles (CFA) : installations électriques Haute Tension HTA, Basse Tension (HTBT), éclairage public et éclairage tunnels, Vidéosurveillance, Sonorisation, Télécom (réseaux IP, fibre optique, radio,…), Information Voyageurs/Usagers, Gestion Technique Centralisée, Supervision et Hypervision, etc… :\nEtudes : Diagnostic, Etudes Préliminaires (EP), Avant-Projet (AVP), Projet (PRO), Assistance à la passation des contrats de travaux (ACT) ;\nTravaux : VISA et Etudes d’exécution (EXE), suivis des travaux (DET) et assistance aux opérations de réception (AOR).\nMais aussi :\nVous serez associé à la réalisation d’offres commerciales et techniques dans les domaines CFO et CFA.\nDes déplacements hebdomadaires sont à prévoir au niveau national.\nPossibilités d’évolution\nChez Ingérop et en fonction de vos appétences, vos compétences techniques ainsi que vos qualités de conduite de projet, de développement commercial et entrepreneuriales vous permettent d'évoluer vers un poste d’Adjoint Chef de service ou de Chef de service.\nQualifications\nDe formation ingénieur, Master II ou Bac+5 (CentraleSupélec, IMPGT, IMT, HEI, etc) dans le domaine électricité, automatismes et informatique industrielle.\nVous justifiez de 3 à 5 ans d’expérience dont 2 ans d’expérience minimum comme ingénieur(e) d’études spécifiquement en CFO et CFA.\nLa maîtrise de l’outil CANECO, Dialux et Relux 3D sera quant à elle appréciée.\nVous êtes organisé, autonome, curieux, doté d’agilité dans la communication tant orale qu’écrite.\nInformations complémentaires\nVotre package :\nVotre rémunération fixe mensuelle\nUne charte télétravail\nL’acquisition de jours de RTT\nUn Compte Epargne Temps (CET)\nLe droit à des CESU\nL’accès à l’épargne salariale / l’intéressement / la participation\nL’affiliation à une mutuelle et une prévoyance de qualité\nUne politique de formation individualisée et des parcours métiers\nL’accompagnement de votre évolution professionnelle et de vos souhaits de mobilité géographique\nUn CSE dynamique\nIngérop attache de l’importance à la diversité de ses équipes et agit pour l'insertion des personnes en situation de handicap. Nous étudions chaque candidature à compétences égales.\nVotre engagement, notre ambition, ensemble inventons demain !\n#LI-Hybrid #EngineeringJobs #NowHiring #JoinOurTeam #IND/INGEROP"
  },
  {
    "id": "1862281304",
    "date_posted": "2025-09-02T10:50:49.927",
    "date_created": "2025-09-02T10:53:05.385872",
    "title": "STELLVERTRETENDE/R FILIALLEITER/IN (M/W/D) - Trostberg",
    "organization": "JYSK",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Altöttinger Straße",
          "addressLocality": "Trostberg",
          "addressRegion": "Bavaria",
          "postalCode": "83308",
          "addressCountry": "Germany"
        }
      }
    ],
    "locations_alt_raw": [
      "Altöttinger Str., 83308 Trostberg, Deutschland"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Vollzeit"
    ],
    "url": "https://jobs.smartrecruiters.com/JYSK/744000079451723-stellvertretende-r-filialleiter-in-m-w-d-trostberg",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Trostberg"
    ],
    "counties_derived": [
      "Landkreis Traunstein"
    ],
    "regions_derived": [
      "Bavaria"
    ],
    "countries_derived": [
      "Germany"
    ],
    "locations_derived": [
      "Trostberg, Bavaria, Germany"
    ],
    "timezones_derived": [
      "Europe/Berlin"
    ],
    "lats_derived": [
      48.03787308493265
    ],
    "lngs_derived": [
      12.56043005770898
    ],
    "remote_derived": false,
    "domain_derived": "jysk.com",
    "description_text": "Stellenbeschreibung\nEs macht dir Spaß, deine Kollegen zu motivieren, gemeinsam die besten Ergebnisse zu erreichen? Du willst jeden Tag ein Stückchen besser werden? Du erkennst Möglichkeiten, wo andere Hindernisse sehen, und willst mit deinem Team für das beste Einkaufserlebnis unserer Kunden sorgen?\nDann ist die Stelle als stellvertretender Filialleiter das perfekte Match für dich!\nWAS WIR DIR BIETEN\nJYSK hat es sich als Ziel gesetzt, die erste Wahl der Mitarbeiter im Einzelhandel zu sein. Jetzt hast du die Chance, ein Teil davon zu werden und zusammen mit uns an diesem großen Ziel zu arbeiten!\nJYSK ist ein dynamisches Unternehmen und bei uns wird deine Stimme gehört. Du wirst involviert und deine Entwicklung ist uns sehr wichtig. Um dich in deiner Rolle als stellvertretender Filialleiter bestmöglich zu stärken, bieten wir dir:\nMöglichkeiten für deine eigene Entwicklung durch ausgezeichnetes Training und Mentoring\nFlexible Arbeitszeitgestaltung mit einem arbeitsfreien Samstag im Monat\n20% Mitarbeiterrabatt\nUrlaubs- und Weihnachtsgeld sowie umsatzorientierte Bonuszahlungen\nBetriebliche Altersvorsorge und ein AG-Zuschuss zur Entgeltumwandlung von 30%\nExklusive Mitarbeitervorteile und Zugang zu zahlreichen Corporate Benefits \nSteuerfreies Gehaltsextra mit einer mtl. Sachbezugskarte in Höhe von bis zu 50€\nInterne Wettbewerbe mit attraktiven Prämien sowie Teamevents und unsere Jahresfeier\n36 Tage Urlaub\nWAS BEINHALTET DEINE NÄCHSTE STELLE\nGemeinsam mit der Filialleitung bist du für eine JYSK-Filiale verantwortlich\nEntsprechend der JYSK-Werte unterstützt du deine Filialleitung bei der Weiterentwicklung des Filialteams auf der Verkaufsfläche\nDu ergreifst die Initiative, um Kennzahlen positiv zu beeinflussen und motivierst das Team, großartige Ergebnisse zu erzielen\nDu setzt die Filialkonzepte und -routinen um und hältst diese nach\nDu magst Bewegung und körperliche Arbeit und agierst als Vorbild, indem du zusammen mit der Filialleitung, die Verantwortung im Verkauf und den Routineaufgaben in der Filiale übernimmst\nWAS SOLLTEST DU MITBRINGEN\nFür uns zählt deine Einstellung, alles andere können wir dir beibringen, deswegen sind Quereinsteiger auch herzlich willkommen\nDu bist inspirierend und kommunikativ und schaffst hierdurch eine positive Arbeitsumgebung\nDu strebst immer danach, die besten Ergebnisse zu erzielen\nSelbst in stressigen Situationen bleibst du fokussiert und motivierst dein Team\nDu bist bereit, auch an Samstagen zu arbeiten und hast dafür einen Tag in der Woche frei\nDu brennst für den Verkauf und bist ein kompetenter Kundenberater\nIST DAS DEINE NÄCHSTE CHANCE? Bewirb dich noch heute!\nÜber uns\nWir sind überzeugt, dass unsere Mitarbeiter der Schlüssel zu unserem Erfolg sind. Deshalb setzen wir alles daran, Entwicklungsmöglichkeiten zu bieten und neue Herausforderungen innerhalb von JYSK zu schaffen. Seit unser Gründer, Lars Larsen, 1979 sein erstes Geschäft in Dänemark eröffnet hat, haben wir unsere globale Präsenz mit Filialen und Onlineshops in vielen Ländern weltweit ausgebaut.\nHinweis: In unseren Stellenanzeigen wird aus Gründen der besseren Lesbarkeit die männliche Form der Anrede verwendet. Die weibliche/ diverse Form ist stets mit eingeschlossen, denn Menschen sind vielfältig. Bei JYSK sind alle Menschen unabhängig von ihrem Geschlecht, Alter, Religion, Behinderung, ethnischer Herkunft oder sexueller Identität willkommen\nLies in unseren Datenschutzhinweisen mehr darüber, wie wir Deine Daten verarbeiten."
  },
  {
    "id": "1862281298",
    "date_posted": "2025-09-02T10:50:42.222",
    "date_created": "2025-09-02T10:53:04.986744",
    "title": "Project Engineer",
    "organization": "NAVANTIA UK",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Arnish Point",
          "addressLocality": "Stornoway",
          "addressRegion": "Isle of Lewis",
          "postalCode": "HS2 9JZ",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "Arnish Point, Stornoway, Isle of Lewis, United Kingdom"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/NAVANTIAUK/744000079455625-project-engineer",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Stornoway"
    ],
    "counties_derived": [
      "Na h-Eileanan an Iar"
    ],
    "regions_derived": [
      "Scotland"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Stornoway, Scotland, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      58.208221
    ],
    "lngs_derived": [
      -6.392546
    ],
    "remote_derived": false,
    "domain_derived": "navantia.es",
    "description_text": "Company Description\nNavantia UK isn’t just another engineering company. Following the exciting acquisition of Harland & Wolff’s world-class facilities, we’re on a mission to strengthen Britain’s defence, maritime, and clean energy capabilities. With big growth ahead in the energy sector, this is your chance to be part of a company with ambition, heritage, and a future full of opportunity.\nAt Arnish, you’ll play a key role in projects that power communities, protect nations, and shape the clean energy transition. If you’re ready for a challenge that comes with impact, this is the place for you.\nJob Description\nProject Engineer – Build the Future with Navantia UK\nThe Role\nAs a Project Engineer, you’ll be the vital link between design and operations – turning plans into action and ideas into results. You’ll support bids, guide projects technically, and ensure that engineering solutions are smart, safe, and efficient. Every day will bring a new challenge – from problem-solving on complex systems to coordinating with partners across multiple disciplines.\nThis role isn’t about sitting back – it’s about making things happen.\nWhat You’ll Do\nBreak down complex engineering tasks (maintenance, refit, and new build) into project plans that deliver results.\nShape and maintain schedules, resource plans, and delivery frameworks that keep projects on track.\nDevelop production- and cost-friendly solutions that still meet the highest technical standards.\nMonitor progress, risks, and variations – keeping everything aligned with budgets, milestones, and quality.\nWork closely with internal teams, subcontractors, and clients – making sure everyone pulls in the same direction.\nPrepare specs, select equipment, and support bids, tenders, and budgets.\nDrive continuous improvement and share lessons learned to strengthen future projects.\nMentor and support junior engineering staff – helping to build the next generation of talent.\nBe the problem-solver when things get tough – finding innovative solutions and ensuring issues are resolved.\nQualifications\nWhat You’ll Bring\nA degree in Engineering (or HNC/HND with significant experience).\nProject management skills (APM accreditation a plus; APM/Prince2 qualifications desirable).\nExperience with project tools like Primavera P6, Microsoft Office Suite, and ERP systems (SAP/IFS a bonus).\nKnowledge of project management and process improvement techniques.\nStrong communication and relationship-building skills – you’re confident with clients and colleagues alike.\nThe ability to juggle multiple high-priority projects while keeping calm under pressure.\nA solid understanding of HSE requirements.\nA problem-solving mindset that seeks out innovative, practical solutions.\nEligibility for Baseline Clearance.\nAdditional Information\nWhat’s in it for You?\nCompetitive salary\n31 days holiday\nCompany pension\nOvertime opportunities\nOnsite parking\nThe chance to work on projects that matter – from renewable energy to national defence\nThis isn’t just a job. It’s a career with purpose, growth, and the chance to make your mark on some of the UK’s most exciting industrial projects.aa\nReady to engineer the future with us?\nApply today, or if you’re having trouble with the online process, email us at [email protected] and our team will be happy to help.\nIf you experience difficulties or are unable to apply for a role on-line please contact us at [email protected] and one of the team will be in contact to help you."
  },
  {
    "id": "1862281303",
    "date_posted": "2025-09-02T10:50:03.572",
    "date_created": "2025-09-02T10:53:05.348926",
    "title": "Care Assistant",
    "organization": "City and County Healthcare Group Ltd",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Mona",
          "addressRegion": "Wales",
          "postalCode": "LL77 7EQ",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "Mona, Llangefni LL77 7EQ, UK"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/CityCountyHealthcareGroupLtd/744000079454732-care-assistant",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Llangefni"
    ],
    "counties_derived": [
      "Isle of Anglesey"
    ],
    "regions_derived": [
      "Wales"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Llangefni, Wales, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      53.248028149999996
    ],
    "lngs_derived": [
      -4.361254254079192
    ],
    "remote_derived": false,
    "domain_derived": "candchealthcare.co.uk",
    "description_text": "Company Description\nLocation: Anglesey\nPay Rate: £13.50 per hour\nShifts Available: 24 Hour Package With Sleeping Nights - 8am - 8am (1:1)\nAccess to a vehicle required due to the geographical location of the role. \nWhat we offer\nComplete Care Amegreen is part of City & County Healthcare Group. You’ll have access to all the resources, career pathways, benefits, investments, opportunities, and security that being part of City & County Healthcare Group brings. It’s the best of both worlds.\nWe're sorry, but we do not currently offer sponsorship to applicants.\nWhat you’ll get\nMaternity/Paternity leave\nPension scheme\nPaid annual leave\nRefer a friend scheme\nCycle-to-work scheme\nEnhanced DBS check\nJob Description\nWhat you’ll do\nThis is an excellent opportunity to enhance your current skill base and join us as a Complex Care Assistant. You will have full training and clinical support to develop and enhance skills in various complex areas such as tracheotomy, ventilation, seizure management, and stoma care plus so much more! We care for and support people of all ages, in the community, and in their homes, with Spinal Cord injury, Muscular dystrophy, acquired brain injuries and many other complex needs. Every day will be different. And you’ll never know what challenges you’re about to face next. One thing you can be sure of though, is that you’ll be making your clients’ days brighter, whilst developing your skills and knowledge.\nQualifications\nExperience in complex care is desirable, but is not essential as we provide full nurse-led training. However it is extremely advantageous if you have experience in the following:\nTracheostomy\nVentilation Support\nSeizure Management\nPEG Feeding\nSuctioning\nCatheter Care\nBowel Management\nAdministrating Medication\nChallenging Behaviours\nMoving & Handling Equipment\nA full UK driving licence is essential for this role.\nAdditional Information\nWhy choose us?\nWe're an equal opportunities employer. Thanks to the commitment of our health care assistants, we see extraordinary achievements happen every day. We are transforming the care industry by working smarter, using innovative tech and driving forward positive change. As the largest care company in the UK, we have care assistant vacancies across the country, and we offer a world of career opportunity, choice and security.\nApply Today!\nKeywords: Carer, Care Assistant, Care Professional, Care Worker, Healthcare Assistants, Support Workers"
  },
  {
    "id": "1862281300",
    "date_posted": "2025-09-02T10:49:52.379",
    "date_created": "2025-09-02T10:53:05.109701",
    "title": "Conseiller/ Conseillère Service Client CDI - Temps plein (H/F)",
    "organization": "BOULANGER",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Rue Jacques Anquetil 2",
          "addressLocality": "Mérignac",
          "addressRegion": "Nouvelle-Aquitaine",
          "postalCode": "33700",
          "addressCountry": "France"
        }
      }
    ],
    "locations_alt_raw": [
      "2 Rue Jacques Anquetil, 33700 Mérignac, France"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Temps complet"
    ],
    "url": "https://jobs.smartrecruiters.com/Boulanger/744000079455505-conseiller-conseillere-service-client-cdi-temps-plein-h-f-",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Mérignac"
    ],
    "counties_derived": [
      "Gironde"
    ],
    "regions_derived": [
      "New Aquitaine"
    ],
    "countries_derived": [
      "France"
    ],
    "locations_derived": [
      "Mérignac, New Aquitaine, France"
    ],
    "timezones_derived": [
      "Europe/Paris"
    ],
    "lats_derived": [
      44.831127
    ],
    "lngs_derived": [
      -0.659075
    ],
    "remote_derived": false,
    "domain_derived": "boulanger.com",
    "description_text": "Description de l'entreprise\nDepuis plus de 70 ans, Boulanger accompagne les Français dans leur quotidien grâce à une expertise reconnue en électroménager et multimédia. Avec plus de 220 magasins et une présence forte sur Boulanger.com, nous faisons de la satisfaction client notre priorité.\nNotre singularité ? 🌟\nChez Boulanger, tout commence avec le client. Notre ambition est d'offrir une expérience d'excellence grâce à des collaborateurs passionnés, animés par l'envie de se dépasser et d’innover ensemble.\nNos valeurs 💡\nPro : Nous mettons notre expertise au service de nos clients, avec rigueur et engagement.\nSimple : Nous privilégions une approche accessible et des solutions claires.\nSympa : Nous cultivons la bonne humeur et des relations humaines authentiques.\nRejoindre Boulanger, c’est évoluer dans une entreprise qui valorise les talents, offre des opportunités de développement et place la collaboration au cœur de son succès.\n\nApprendre, grandir, réussir : Boulanger, osons ensemble !\nDescription du poste\nRattaché au Responsable Service Client, tu joues un rôle clé pour aider nos clients.\n🎯 Une journée chez Boulanger c’est :\nFaire briller l’accueil client. Comment ? En accueillant chaque client rapidement et en les accompagnant avec professionnalisme pour une satisfaction garantie.\nAssurer les encaissements. Comment ? En suivant les procédures et en veillant à chaque détail pour une expérience fluide et agréable.\nSimplifier le financement. Comment ? En créant des dossiers de financement et apportant des réponses claires pour aider chaque client à concrétiser ses achats.\nOptimiser le retrait des produits. Comment ? En faisant en sorte que les produits soient prêts rapidement, tout en proposant des accessoires pour enrichir l’expérience.\nGérer le SAV avec efficacité. Comment ? En trouvant des solutions adaptées et en offrant un accompagnement personnalisé qui fait la différence.\nFidéliser tes clients. Comment ? En présentant les programmes de fidélité et en construisant une relation de confiance durable.\nOffrir une expérience premium. Comment ? En anticipant les attentes des clients et en leur proposant des solutions sur-mesure pour dépasser leurs attentes.\nQualifications\nTu es fait pour ce job si :\nLe service client, c’est ta force\nRéactivité et rigueur sont tes alliés\nL’écoute, c’est innée\nLe bon communiquant, c’est toi\nSi, comme nous, tu es engagé et authentique, si tu es généreux dans tes échanges et agile dans tes actions, alors rejoins notre collectif pro, simple, sympa, et osons ensemble ! \n\n💰 Rémunération : \nFixe : 23 600 € sur 13 mois + variable collective mensuelle \nPrimes attractives : Participation aux bénéfices, primes d’intéressement trimestrielles, et l’actionnariat salarié… \nConditions avantageuses : une mutuelle qui couvre l’ensemble de ton foyer, prévoyance, carte restaurant, forfait mobilité durable\nInformations complémentaires\n📣 Pourquoi nous rejoindre ?\n\nChez nous, l'expérience compte, mais ta personnalité et ton envie d'apprendre sont encore plus précieux !\nFormation “48h du commerce” : Une fois par an, tu vivras cet évènement au siège. Un événement unique où tu découvriras les dernières innovations technologiques avec 900 collègues et plus de 50 formateurs internes passionnés !\nAvantages exclusifs : Profite de belles remises sur nos produits et des offres spéciales en tant que membre du club+ Boulanger.\nEngagement pour l’inclusion : Notre indice de parité est de 89/100, preuve de notre engagement pour l’égalité.\nResponsabilité sociétale : redonner une seconde vie aux produits, c’est un engagement fort. Chez Boulanger, chaque magasin participe à ce geste éco-responsable."
  },
  {
    "id": "1862281301",
    "date_posted": "2025-09-02T10:49:42.47",
    "date_created": "2025-09-02T10:53:05.19079",
    "title": "Senior Sous Chef",
    "organization": "WSH Group",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Manton Lane",
          "addressLocality": "Bedford",
          "addressRegion": "England",
          "postalCode": "MK41",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "Manton Ln, Bedford MK41, UK"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/WSHGroup/744000079455485-senior-sous-chef",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Bedford"
    ],
    "counties_derived": [
      "Bedford"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Bedford, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      52.14798456000251
    ],
    "lngs_derived": [
      -0.4776666233531362
    ],
    "remote_derived": false,
    "domain_derived": "baxterstorey.com",
    "description_text": "Company Description\nSenior Sous Chef \nLocation: Bedford Modern School, Manton Lane, Bedford MK41 7NT\nRate of pay: £29,000 - £30,000pa\nHours: 40 hours per week\nWeeks: 40 weeks\nBenefits:\n28 days holiday \n3 volunteering days\n3 days grandparent leave\n24 week’s enhanced maternity leave\nBespoke training and development opportunities\nPension and life insurance\nDiscounts available on our Perkbox app; high street shops, holidays & cinema\nWellbeing hub\nAccess to employee assistance programme\nFree meals whilst at work\nCareer development opportunities\nHIT Apprenticeships for all experience levels\nWe currently have an exciting opportunity for a Senior Sous Chef with a background in exceptional food catering services to join us at one of our highly prestigious education settings. This prestigious independent school caters for students age 7-18 comprising a junior school and a senior school. With over 1,200 students, the school has a deep rooted history going back to 1764.\nIf you are passionate about creating delicious dining experiences that fuel young minds and ignite taste buds, then this is the perfect opportunity to bring your expertise to our table.\nJob Description\nKey Responsibilities\nTo assist the chef team in planning, preparing, cooking and presenting food to the standards required by the company and the client.\nTo control portion size and monitor waste\nTo ensure supplies are correctly used, accounted for and to assist with weekly stock take and food rotation procedures\nTo maintain records relating to food production activities and supplier information as required by the catering manager\nTo ensure Health and Safety and Food Safety Standards are maintained in line with company policy and legislation\nTo assist the executive chef in the day to day running of the kitchen\nTo assist in regular team meetings on a regular basis to communicate targets, standards required and company/client information\nTo ensure compliance with the company's policy on safer recruitment and safeguarding children and young adults at all times whilst at work.\nQualifications\nExcellent communication skills\nTakes the initiative\nExcellent time management\nSupportive / Team player\nDemonstrate high level of organisation.\nExcellent record keeping.\nTo be willing to work the hours and the needs of the business\nTo be able to work under pressure and to cope with any unforeseen circumstances i.e. function changes, requirements, sickness, etc.\nTo have a positive and co-operative attitude.\nAdditional Information\nHolroyd Howe is one of the UK’s leading contract caterers, providing fresh innovative food services solely to independent schools and colleges. We are a team of experienced professionals who tailor our catering service provision specifically to suit children of all ages in order to meet the bespoke requirements of each school.\nTo provide our teams with the right skills to succeed in their jobs, we invest in their training and development. Our exceptional teams of seasoned specialists customise our catering services to fit children of all ages and satisfy the unique needs of our clients.\nWe pride ourselves on:\nSustainability\nSustainability is at the heart of our thinking; always mindful of the ethics of our sourcing and how we prepare our meals.\nNutrition\nWe take nutrition seriously and understand the impact a healthy diet has on the fundamental years of development. Meals are always freshly prepared from scratch and packed with nutritious ingredients.\nFood Innovation\nWe offer a wide portfolio of training opportunities and experiences, which attracts chefs who are passionate about culinary excellence and menu innovation to our team.\nFrom tasting tables, theme days and food theatre, to chef demonstrations and supplier showcases, we create engaging and fun dining experiences for our students. We work together to make mealtimes exploratory, quirky, and fun for our pupils, helping them build strong and healthy relationships with food.\nHolroyd Howe is an equal opportunities employer. We are committed to safeguarding and promoting the welfare of children and young people and expect all employees to share this commitment. All roles within Holroyd Howe involve regulated activity. It is a criminal offence for individuals barred from working with children to apply for such roles. An Enhanced Disclosure and Barring Service (DBS) check, including a Barred List check will be required for all successful applicants. Shortlisted applicants will be asked to provide information about relevant criminal offences and will be subject to an online search of publicly available information. This search helps identify any issues that may affect suitability to work with children.\nThis appointment is offered on the return of satisfactory professional references.\nIND1"
  },
  {
    "id": "1862281302",
    "date_posted": "2025-09-02T10:49:30.762",
    "date_created": "2025-09-02T10:53:05.26575",
    "title": "Ecommerce Director (Retail Media)",
    "organization": "Jellyfish",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Bengaluru",
          "addressRegion": "Karnataka",
          "addressCountry": "India"
        }
      }
    ],
    "locations_alt_raw": [
      "Bengaluru, Karnataka, India"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/Jellyfish1/744000079453796-ecommerce-director-retail-media-",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Bengaluru"
    ],
    "counties_derived": [
      "Bangalore North"
    ],
    "regions_derived": [
      "Karnataka"
    ],
    "countries_derived": [
      "India"
    ],
    "locations_derived": [
      "Bengaluru, Karnataka, India"
    ],
    "timezones_derived": [
      "Asia/Kolkata"
    ],
    "lats_derived": [
      12.9767936
    ],
    "lngs_derived": [
      77.590082
    ],
    "remote_derived": false,
    "domain_derived": "jellyfish.com",
    "description_text": "Company Description\nAt Jellyfish, we believe in the power of diverse perspectives and inclusive collaboration. We welcome individuals who excel in collaborative, varied teams and value the unique contributions that each person brings to the table.\nJellyfish is a global digital marketing agency; a unique fusion of tech enthusiasts, creative minds, and media and data experts all united to empower our clients along their digital journey. Our commitment to embracing diverse perspectives fuels our innovation and strategies that challenge the status quo, reinvent media activation, and craft influential stories for our global clients and their customers. Join us in shaping a future where business growth and personal fulfilment go hand in han\nJob Description\nReporting to the Senior Retail Media Director, as a Retail Media Director, you will be an important contributor in leading media strategy and team development. Your main responsibilities will include management and growth of a portfolio of accounts, driving business conversations with clients, and developing successful Retail Media strategies through cross-disciplinary collaboration. Success in this position requires the ability to tell stories from data, the ability to function in a team-focused environment, and the willingness to exemplify Jellyfish's core values (be accountable, be positive, be passionate, be the solution).\nResponsibilities:\nOversee a portfolio of accounts, ensuring client satisfaction and business growth\nBuild strong client relationships and understand their business goals\nCreate and deliver large-scale, data-driven strategies for clients\nProject manage initiatives within the media plan\nCreate professional client-facing documents highlighting clear and actionable performance insights\nCollaborate with Business Development to create innovative strategies for prospective clients\nAlign with leaders across the business to create best practices, develop processes, and promote knowledge-sharing\nMentor and educate junior staff to enhance platform expertise, client performance, and individual's ongoing personal development\nQualifications\nProficiency in overseeing the management & success of a large client portfolio\nDemonstrated expertise of retail media advertising sponsored ads and DSP platforms\nExperience working with Vendor & Seller Central, Amazon Marketing Cloud (AMC) and 3rd party bid management platforms such as Skai or Pacvue\nFamiliarity with demonstrating a structured way of working, with the ability to cope with competing demands\nExperience managing media budgets over $1 million dollars while hitting/outperforming KPIs\nFull funnel media planning experience taking into account several ad formats, audiences, and seasonal periods\nComprehensive understanding of the retail industry\nExperience managing a team\nAdvanced Excel (can perform complex functions) /Google Sheets.\nPreviously worked in EST or similar Night shift hours.\nNote: We emphasise skills, expertise and behavioural attributes over years of experience and traditional degrees. If you want to join our collaborative team, we invite you to apply today with your resume in English.\nAdditional Information\nJoin Jellyfish and experience a workplace where we prioritise your growth, celebrate your contributions, and empower you to tailor your work environment to suit your needs.\n💰 Reward: You'll be eligible to join our discretionary annual bonus scheme.\n💫 Custom Work Environment: Work remotely with night shift.\n📈 Growth, Your Way: Accumulate one paid day each month (2 hours per week) for self-development and access to Jellyfish Learn.\n🏦 Jellyfish contributes to your retiral benefits via Provident Fund (PF) contribution\nJellyfish provides best in class group medical insurance & life insurance cover to employees\nUnfortunately, there has been an increase in fake recruiters impersonating Jellyfish and unlawfully using our brand name. If you are unsure if an email with a job offer you have received is genuinely from Jellyfish, or if you suspect any fraudulent activity, please report it to [email protected]."
  },
  {
    "id": "1862281299",
    "date_posted": "2025-09-02T10:49:18.73",
    "date_created": "2025-09-02T10:53:05.087975",
    "title": "Senior Lighting Engineer",
    "organization": "AECOM",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "addressLocality": "Chesterfield",
          "addressCountry": "United Kingdom"
        }
      }
    ],
    "locations_alt_raw": [
      "Chesterfield, United Kingdom"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Full-time"
    ],
    "url": "https://jobs.smartrecruiters.com/AECOM2/744000079454842-senior-lighting-engineer",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Chesterfield"
    ],
    "counties_derived": [
      "Derbyshire"
    ],
    "regions_derived": [
      "England"
    ],
    "countries_derived": [
      "United Kingdom"
    ],
    "locations_derived": [
      "Chesterfield, England, United Kingdom"
    ],
    "timezones_derived": [
      "Europe/London"
    ],
    "lats_derived": [
      53.2352134
    ],
    "lngs_derived": [
      -1.4264097
    ],
    "remote_derived": false,
    "domain_derived": "aecom.com",
    "description_text": "Company Description\nWork with Us. Change the World.\nAt AECOM, we're delivering a better world. Whether improving your commute, keeping the lights on, providing access to clean water, or transforming skylines, our work helps people and communities thrive. We are the world's trusted infrastructure consulting firm, partnering with clients to solve the world’s most complex challenges and build legacies for future generations.\nThere has never been a better time to be at AECOM. With accelerating infrastructure investment worldwide, our services are in great demand. We invite you to bring your bold ideas and big dreams and become part of a global team of over 50,000 planners, designers, engineers, scientists, digital innovators, program and construction managers and other professionals delivering projects that create a positive and tangible impact around the world.\nWe're one global team driven by our common purpose to deliver a better world. Join us.\nJob Description\nStart here. Grow here. \nOur Lighting Team is seeking a Senior Lighting Engineer to drive the future of lighting across the UK. This role offers an exciting opportunity to influence infrastructure projects from conception through completion.\nEach team member has a development plan to provide a clear pathway to personal development and career progression. The team provides technical leadership of projects throughout the infrastructure lifecycle from feasibility, preliminary and detailed stage designs in some cases through construction.\nOur clients are many and varied from the private and public sector working with numerous local authorities, we work with internal client from transport, rail etc.\nHere’s what you’ll do:\nDevelop: Manage engineering tasks, explore subject areas, define project scopes, and create unique solutions.\nAdvise: Provide expert technical knowledge and support across multi-disciplinary projects.\nDesign: from conceptual stages to implementation which will include site visits, lighting designs, private cable calculation designs, CAD designs, production of lighting specifications, Bills of Quantities and liaison with DNO suppliers.\nEnsure Quality: Strong efficiencies on quality and budget control on projects, navigate the complexities of transportation and landscape projects, working with clients to address and resolve challenges.\nCollaborate: Build strong relationships with technical teams and clients, leading multi-disciplinary efforts to achieve integrated design solutions.\nCome grow with us:\nAnd let's not forget about the perks at AECOM. You'll enjoy a range of core and personalised benefits designed to support your future and well-being, customized to fit your lifestyle. Take advantage of career development opportunities, our flexible hybrid working model to ensure a work-life balance that suits your lifestyle, technical practice networks, AECOM University, and volunteering days. \nQualifications\nReady to push the limits of what’s possible? \nRequirements:\nRelevant Technical Qualifications: Ideally, you possess an ILP Exterior Lighting Diploma or equivalent qualification in a related technical field.\nProven Design Experience: Demonstrated success in a lighting design environment, with a proactive and creative approach to problem-solving.\nSoftware Proficiency: Proficient in industry-standard software, including Lighting Reality, AGi32, Dialux, and Amtech Pro Design to create and assess detailed lighting schemes.\nStrong Communication and Interpersonal Skills: Exceptional written and verbal communication skills, with the ability to confidently and diplomatically engage with staff, colleagues, and clients.\nProject Management: Oversee project timelines, budgets, and resources to ensure projects are delivered on schedule, within budget, and to the highest quality standards. Manage client expectations and project requirements from inception through to completion.\nAdditional Information\nAt AECOM, we value everyone's unique contributions and perspectives. If you meet some of the requirements above or have transferable skills you believe would benefit us, we would be delighted to hear from you!\nInterested in the role or curious about life at AECOM? Follow us on LinkedIn, Facebook, Instagram, and YouTube to explore our AECOM voices, employee stories, latest projects, and much more! \nWorking locations is flexible across the UK (Hybrid - office/remote working), while attendance will be required a nearest local office from time to time (minimum once a week).\nAbout AECOM\nAECOM is the world’s trusted infrastructure consulting firm, delivering professional services throughout the project lifecycle – from advisory, planning, design and engineering to program and construction management. On projects spanning transportation, buildings, water, new energy and the environment, our public- and private-sector clients trust us to solve their most complex challenges. Our teams are driven by a common purpose to deliver a better world through our unrivaled technical and digital expertise, a culture of equity, diversity and inclusion, and a commitment to environmental, social and governance priorities. AECOM is a Fortune 500 firm and its Professional Services business had revenue of $14.4 billion in fiscal year 2023. See how we are delivering sustainable legacies for generations to come at aecom.com and @AECOM.\nFreedom to Grow in a World of Opportunity \nYou will have the flexibility you need to do your best work with hybrid work options. Whether you’re working from an AECOM office, remote location or at a client site, you will be working in a dynamic environment where your integrity, entrepreneurial spirit and pioneering mindset are championed.\nYou will help us foster a safe and respectful workplace, where we invite everyone to bring their whole selves to work using their unique talents, backgrounds and expertise to create transformational outcomes for our clients.\nAECOM provides a wide array of compensation, benefits and well-being programs to meet the diverse needs of our employees and their families. We’re the world’s trusted global infrastructure firm, and we’re in this together – your growth and success are ours too.\nJoin us, and you’ll get all the benefits of being a part of a global, publicly traded firm – access to industry-leading technology and thinking and transformational work with big impact and work flexibility. As an Equal Opportunity Employer, we believe in each person’s potential, and we’ll help you reach yours.\nWe are a Disability Confident Employer and will offer an interview to applicants who have a disability or long-term condition, who meet the minimum/essential criteria for the role. Please let us know using this email address [email protected] if you would like to apply through the Disability Confident Interview Scheme.\nAll your information will be kept confidential according to EEO guidelines."
  },
  {
    "id": "1862281309",
    "date_posted": "2025-09-02T10:49:12.99",
    "date_created": "2025-09-02T10:53:07.531848",
    "title": "CHEF DE PROJET VRD INDUSTRIELS F/H",
    "organization": "Ingérop",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Avenue Georges Pompidou 23",
          "addressLocality": "Lyon",
          "addressRegion": "Auvergne-Rhône-Alpes",
          "postalCode": "69003",
          "addressCountry": "France"
        }
      }
    ],
    "locations_alt_raw": [
      "23 Av. Georges Pompidou, 69003 Lyon, France"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Temps complet"
    ],
    "url": "https://jobs.smartrecruiters.com/Ingrop/744000079455387-chef-de-projet-vrd-industriels-f-h",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "Lyon"
    ],
    "counties_derived": [
      "Métropole de Lyon"
    ],
    "regions_derived": [
      "Auvergne-Rhône-Alpes"
    ],
    "countries_derived": [
      "France"
    ],
    "locations_derived": [
      "Lyon, Auvergne-Rhône-Alpes, France"
    ],
    "timezones_derived": [
      "Europe/Paris"
    ],
    "lats_derived": [
      45.7593442
    ],
    "lngs_derived": [
      4.8653291
    ],
    "remote_derived": false,
    "domain_derived": "ingerop.fr",
    "description_text": "Description de l'entreprise\nRejoindre Ingérop, c’est contribuer à façonner le monde de demain.\nGroupe d’ingénierie et de conseil indépendant, nous menons des projets ambitieux dans les domaines du bâtiment, de l’énergie, de l’industrie, de l’eau, des infrastructures, des transports et de la ville.\nAvec plus de 40 sites en France, 98 implantations dans le monde et plus de 3 500 collaborateurs, nous offrons de nombreuses opportunités, en conception comme en réalisation, en local comme à l’international.\nChez Ingérop, vous évoluerez dans un environnement innovant, humain et solidaire, où l’expertise, l’esprit d’équipe et la convivialité sont au cœur de notre culture. Rejoignez une communauté de passionnés !\nDescription du poste\nEtes-vous prêt à relever un défi captivant dans le monde de l'ingénierie ? Notre unité Alpes Centre Est (500 collaborateurs), recherche un Chef de projet VRD Industriels, motivé et curieux dans le service ville pour rejoindre notre équipe dynamique. \nVous serez rattaché au Chef de service de l’agence de Clermont-Ferrand, en restant basé à l’agence de Lyon avec forte autonomie. Vous réaliserez principalement des missions de maîtrise d'oeuvre et de coordination des projets. \nA partir du cahier des charges du client et de l'offre Ingérop, vous veillerez à assurer la réalisation de tous les volets des contrats qui vous sont confiés :\nOrganiser la mission ;\nSe coordonner avec l'équipe projet du client ;\nSe coordonner avec l'équipe projet en interne ;\nProduire les dossiers de compétences dans le respect du besoin du client et du contrat ;\nGérer l'ensemble des réunions nécessaires ;\nRendre compte au responsable d'exploitation et solliciter les expertises internes ou externes ;\nSuivre son activité et son budget.\nLes compétences techniques exigées portent sur les domaines techniques de projets d’aménagements industriels privés diversifiés :\nVoiries,Terrassements / géotechniques ;\nRéseaux humides ;\nRéseaux utilités ;\nHydraulique / gestion des eaux pluviales et eaux incendie ;\nInfrastructures courants forts et courants faibles ;\nIntégration des objectifs environnementaux et certification (LEED, BREEAM, etc …)\nUne expertise dans l'un ou plusieurs des domaines ci-dessus sera appréciée.\nQualifications\nVous êtes titulaire d'une formation Bac + 5 de type ingénieur ou master 2 et avez 10 ans d'expérience minimum dans un poste similaire, orienté aménagements privés/industriels, infrastructures, ou justifiant d'une expérience significative dans le domaine de la VRD.\nVous êtes :\nReconnu(e) pour votre capacité à travailler en autonomie ainsi que pour votre rigueur et adaptabilité ;\nDynamique et sociable, en mesure d'animer et motiver une équipe projet ;\nA l'aise avec l'environnement de la construction et de l'aménagement urbain ;\nApte au dialogue et à la négociation ;\nSensible aux enjeux environnementaux.\nInformations complémentaires\nVotre package :\nVotre rémunération fixe mensuelle\nUne charte télétravail\nL'acquisition de jours de RTT\nUn Compte Epargne Temps (CET)\nLe droit à des CESU\nL'accès à l'épargne salariale / l'intéressement / la participation\nL'affiliation à une mutuelle et une prévoyance de qualité\nUne politique de formation individualisée et des parcours métiers\nL'accompagnement de votre évolution professionnelle et de vos souhaits de mobilité géographique\nUn CSE dynamique\n\nIngérop attache de l'importance à la diversité de ses équipes et agit pour l'insertion des personnes en situation de handicap. Nous étudions chaque candidature à compétences égales.\n\nVotre engagement, notre ambition, ensemble inventons demain !\n#LI-Hybrid #EngineeringJobs #NowHiring #JoinOurTeam #IND/INGEROP"
  },
  {
    "id": "1862281306",
    "date_posted": "2025-09-02T10:49:10.882",
    "date_created": "2025-09-02T10:53:07.254297",
    "title": "Part Time Satış Danışmanı (İzmir Optimum AVM)",
    "organization": "H&M Group",
    "organization_url": null,
    "date_validthrough": null,
    "locations_raw": [
      {
        "address": {
          "streetAddress": "Akçay Cad. No:103",
          "addressLocality": "İzmir",
          "addressRegion": ".",
          "addressCountry": "Turkey"
        }
      }
    ],
    "locations_alt_raw": [
      "Akçay Cad. No:103, İzmir, ., Türkiye"
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "Yarı zamanlı"
    ],
    "url": "https://jobs.smartrecruiters.com/HMGroup/744000079454692-part-time-sat-s-dan-sman-izmir-optimum-avm-",
    "source_type": "ats",
    "source": "smartrecruiters",
    "source_domain": "jobs.smartrecruiters.com",
    "organization_logo": null,
    "cities_derived": [
      "İzmir"
    ],
    "counties_derived": [
      "Izmir"
    ],
    "regions_derived": [
      "Aegean Region"
    ],
    "countries_derived": [
      "Turkey"
    ],
    "locations_derived": [
      "İzmir, Aegean Region, Turkey"
    ],
    "timezones_derived": [
      "Europe/Istanbul"
    ],
    "lats_derived": [
      38.4192537
    ],
    "lngs_derived": [
      27.128469
    ],
    "remote_derived": false,
    "domain_derived": "hmgroup.com",
    "description_text": "Şirket Tanımı\nNELER YAPACAKSIN\nSatış Danışmanı olarak, mükemmel müşteri deneyimi yaratmada önemli bir rol oynayacaksın. Müşterileri karşılayacak, mağazanda onlara rehberlik edecek ve sergilenen ürünlerimiz arasından ihtiyaç duyduklarını bulmaları için yardımcı olacaksın. Değerlerimiz doğrultusunda hareket ederek, hem kendi başarına hem de şirketin başarısına katkıda bulunacaksın.\nSenden beklenenler:\n→Müşterilerin bilinçli seçimler yapmalarına yardımcı olmak için moda ve ürün bilgini paylaşmak.\n→ Müşteri Sadakat programını (Hello Member) aktif olarak tanıtarak, müşteri yolculuğunun her adımında ekibinizle işbirliği yaparak olağanüstü hizmet sunmak.\n→ Satış alanının ve arka ofisin doğru stok seviyesine sahip, düzenli ve davetkar olduğundan emin olmak.\n→ Mağazanın açılış ve kapanışını desteklemek.\n→ Tüm müşteri etkileşimlerinde kendini ve markayı olumlu bir şekilde temsil etmek.\n​\nKİMLERLE ÇALIŞACAKSINIZ\nMağazalarımız şirketimizin kalbidir, müşterilerimizin markamızı doğrudan deneyimlediği yerlerdir. Dinamik Mağaza Ekibinin bir parçası olarak, Satış Danışmanlarından, Departman Müdürlerinden, Mağaza Müdürlerinden ve Görsel Düzenleme Sorumlularından, Kasa Ofis Sorumlusuna kadar her rol, ilham verici ve misafirperver bir ortam yaratmaya katkıda bulunur. Ayrıca, iç görüleri paylaşmak ve birlikte başarıya ulaşmak için mağazalar arasında iş birliği yaparak Bölge Ekibiyle bağlantı kuracaksın. Birlikte çalıştığın ekiple birlikte, müşterilerin kendilerini güvende hissetmelerine ve en son trendler ve zamansız stillerle bireyselliklerini ifade etmelerine yardımcı olmakta önemli bir rol oynayacaksın. Mağazalarımızdaki müşterilerimizle anlamlı bağlantılar kurarak, modayı herkes için erişilebilir ve sürdürülebilir hale getiriyoruz.\n​\nSENDEN NELER BEKLİYORUZ\nİşte senden beklediğimiz özellikler… \n→ Moda, perakende veya benzer alanlarda müşteri hizmetleri deneyimi tercih sebebi olarak değerlendirilebilir.\n→ Müşterilere yardımcı olma tutkusu ve moda veya perakende ile ilgili olmak – geriye kalanları sana biz öğreteceğiz!\nVe… \n→ İş birlikçi ve dinamik ortamlarda başarılı.\n→ İletişimi güçlü, yaratıcı, mağazacılık teknolojisiyle çalışmaya meraklı, öğrenmeye ve gelişmeye istekli.\n→ Esnek ve eylem odaklı.\nBİZ KİMİZ\nH&M Group, güçlü moda markaları ve girişimlerinden oluşan küresel bir şirkettir. Amacımız, olağanüstü tasarım, uygun fiyatlar ve sürdürülebilir çözümler arasında hiçbir taviz olmadığını kanıtlamaktır. Modayı birçok kişi için özgürleştirmek istiyoruz ve müşterilerimiz aldığımız her kararın merkezinde yer alıyor.\nPaylaştığımız kültür ve değerlerle birleşmiş binlerce tutkulu ve yetenekli meslektaşımızdan oluşuyoruz. Birlikte, gücümüzü, ölçeğimizi ve bilgimizi kullanarak moda endüstrisini daha kapsayıcı ve sürdürülebilir bir geleceğe taşımak istiyoruz.​\nBURADA ÇALIŞMAYI NEDEN SEVECEKSİN\nH&M Group'ta, canlı ve misafirperver bir şirket olmaktan gurur duyuyoruz. Çalışanlarımıza dünya çapında kapsamlı gelişim fırsatlarıyla, cazip avantajlar sunuyoruz.\nTüm H&M Grubu markalarında hem mağazalarda hem de online olarak (H&M, COS, Weekday, Monki, H&M HOME, & Other Stories ve ARKET) %25 personel indirimi.\nH&M Teşvik Programı HIP. Program hakkında daha fazla bilgi edinin. H&M Incentive Program. \nYemek Yardımı\nUlaşım Yardımı\nDoğum Yardımı\nMazeret İzni (Ücretli)\nTaşınma İzni\nDoğum Günü İzni (1 yıl boyunca bizimle çalışma sonrası)\nÖzel durumlar için ilave ücretli izinler (Örnek: ek doğum, hamilelik izinleri)\nYıl Dönümü Kutlaması – 10 yıl ve üzeri bizimle çalışan ekip arkadaşlarımız\nBİZE KATILIN\nBizim benzersizliğimiz, birçok şeyin birleşiminden gelir – kapsayıcı ve işbirlikçi kültürümüz, güçlü değerlerimiz ve büyüme fırsatlarımız. Ancak en önemlisi, bizi biz yapan insanlarımızdır.\nBu, İzmir Optimum AVM'de bulunan yarı zamanlı bir pozisyondur. Başvurunuzu en kısa sürede, ancak en geç 14 Eylül tarihine kadar CV'nizi göndererek yapmanızı rica ederiz. Veri politikaları nedeniyle, yalnızca kariyer sayfası üzerinden yapılan başvuruları kabul ediyoruz.\n​\nBirlikte kariyerinizde bir sonraki adımı atalım. Yolculuk burada başlıyor.​\n*Mağaza Rollerinin Değerlendirilmesi\nSatış Danışmanı pozisyonu için beklenen yüksek başvuru hacmini etkin bir şekilde yönetmek amacıyla, tüm mağazalarımızda yetkinlik bazlı işe alım için çevrimiçi değerlendirme yöntemini kullanıyoruz. Bu, başvuru ve eleme sürecinizin bir parçası olarak çevrimiçi bir değerlendirmeden geçeceğiniz anlamına gelir. Yanıtlarınız, H&M Group tarafından belirlenen önceden tanımlanmış kriterleri uygulayan bir değerlendirme aracı tarafından puanlanacaktır.\nDeğerlendirmeden sonra geri bildirimde bulunma ve soru sorma fırsatına sahipsiniz. Çevrimiçi değerlendirme yöntemiyle ilgili herhangi bir zorluk veya endişeniz varsa, [email protected] adresinden alternatif bir değerlendirme yöntemi talep edebilirsiniz. Alternatif bir yöntemi seçmek, pozisyon için değerlendirilme şansınızı etkilemeyecektir.\nKişisel verilerinizin tarafımızca nasıl işlendiği hakkında daha fazla bilgi için lütfen Gizlilik Politikamızı inceleyin.\n** Adil ve eşit bir süreç yürütüyoruz ve bu nedenle bilinçsiz önyargılara neden olabilecek bir ön yazıyı başvurunuza eklememenizi rica ediyoruz.\nEk Bilgiler"
  }
]