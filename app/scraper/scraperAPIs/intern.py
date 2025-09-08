from scraper_base import JobScraper
from config import ENDPOINTS

class InternScraper(JobScraper):
    def parse_job_data(self, data):
        # Example: flatten nested location info and select relevant fields
        parsed = []
        for item in data:
            parsed.append({
                'id': item.get('id'),
                'title': item.get('title'),
                'organization': item.get('organization'),
                'location': ', '.join(item.get('locations_derived', [])),
                'url': item.get('url'),
                'date_posted': item.get('date_posted'),
                'employment_type': ','.join(item.get('employment_type', [])),
                'remote': item.get('remote_derived'),
            })
        return parsed

if __name__ == "__main__":
    scraper = InternScraper(ENDPOINTS['internships'])
    data = scraper.run(save_csv=True, csv_fields=['id', 'title', 'organization', 'location', 'url', 'date_posted', 'employment_type', 'remote'])
    if data is not None:
        print(f"Scraped {len(data)} internship listings.")
    else:
        print("Failed to scrape internship listings.")

[
  {
    "id": "1862297347",
    "date_posted": "2025-09-02T11:34:54",
    "date_created": "2025-09-02T11:35:18.648802",
    "title": "Co-Op, Site Civil Engineering, Louisville - Spring 2026",
    "organization": "The Kleingers Group",
    "organization_url": "https://www.linkedin.com/company/the-kleingers-group",
    "date_validthrough": "2025-10-02T11:34:54",
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "US",
          "addressLocality": "Louisville",
          "addressRegion": "KY",
          "streetAddress": null
        },
        "latitude": 38.199375,
        "longitude": -85.65353
      }
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "INTERN"
    ],
    "url": "https://www.linkedin.com/jobs/view/co-op-site-civil-engineering-louisville-spring-2026-at-the-kleingers-group-4292765111",
    "source_type": "jobboard",
    "source": "linkedin",
    "source_domain": "linkedin.com",
    "organization_logo": "https://media.licdn.com/dms/image/v2/C4E0BAQE24d3mqmmGgA/company-logo_200_200/company-logo_200_200/0/1644847345173/the_kleingers_group_logo?e=2147483647&v=beta&t=JdYTrNes9rDX94b1KZe68uJLyKBbmq4KcjKbUv50mzQ",
    "cities_derived": [
      "Louisville"
    ],
    "counties_derived": [
      "Jefferson County"
    ],
    "regions_derived": [
      "Kentucky"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Louisville, Kentucky, United States"
    ],
    "timezones_derived": [
      "America/Kentucky/Louisville"
    ],
    "lats_derived": [
      38.2542376
    ],
    "lngs_derived": [
      -85.759407
    ],
    "remote_derived": false,
    "recruiter_name": null,
    "recruiter_title": null,
    "recruiter_url": null,
    "linkedin_org_employees": 148,
    "linkedin_org_url": "http://www.kleingers.com",
    "linkedin_org_size": "51-200 employees",
    "linkedin_org_slogan": "A Destination Company.",
    "linkedin_org_industry": "Civil Engineering",
    "linkedin_org_followers": 3571,
    "linkedin_org_headquarters": "Greater Cincinnati, Ohio",
    "linkedin_org_type": "Privately Held",
    "linkedin_org_foundeddate": "1993",
    "linkedin_org_specialties": [
      "Civil Engineering",
      "Surveying & Mapping",
      "Landscape Architecture",
      "Planning & Urban Design",
      "Sustainable Design (LEED)",
      "Water Resources",
      "Construction Staking",
      "Transportation & Roadway Design",
      "Sports Field Design Services",
      "Safe Routes to School",
      "and ODOT Compliance Standards"
    ],
    "linkedin_org_locations": [
      "6219 Centre Park Dr, Greater Cincinnati, Ohio 45069, US",
      "350 Worthington Road, Suite H, Westerville, Ohio 43082, US",
      "2211 River Rd, Louisville, Kentucky 40206, US",
      "1575 Corporate Woods Pkwy, Uniontown, Ohio 44685, US",
      "2363 1st Avenue North, St. Petersburg, Florida 33713, US",
      "9465 Counselors Row, Suite 200, Indianapolis, Indiana 46240, US"
    ],
    "linkedin_org_description": "Established in 1993, The Kleingers Group provides place-based design solutions for a wide range of public, private, institutional and corporate clients. We focus on providing site civil engineering, transportation engineering, land surveying, landscape architecture, and community planning services.\n\nOur team proudly offers these fully integrated design services with office locations in Cincinnati, Columbus, and Akron, Ohio, Indianapolis, Indiana, St. Petersburg, Florida, and Louisville, Kentucky.  Diverse in size, experience and geography, we strive to apply our creativity and functionality into helping build better communities.",
    "linkedin_org_recruitment_agency_derived": false,
    "seniority": "Internship",
    "directapply": false,
    "linkedin_org_slug": "the-kleingers-group",
    "no_jb_schema": null,
    "external_apply_url": "https://workforcenow.adp.com/mascsr/default/mdf/recruitment/recruitment.html?cid=892cdb29-10a0-47dd-bc91-0d5b26efadcd&ccId=19000101_000001&lang=en_US&source=LI&selectedMenuKey=CurrentOpenings&jobId=545836",
    "expired": null
  },
  {
    "id": "1862298592",
    "date_posted": "2025-09-02T11:25:47",
    "date_created": "2025-09-02T11:36:04.248813",
    "title": "Civil Engineer - Entry Level",
    "organization": "Langan Engineering & Environmental Services",
    "organization_url": "https://www.linkedin.com/company/langan-engineering-environmental-services",
    "date_validthrough": "2025-10-02T11:25:47",
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "US",
          "addressLocality": "Chicago",
          "addressRegion": "IL",
          "streetAddress": null
        },
        "latitude": 41.88323,
        "longitude": -87.6324
      }
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": {
      "@type": "MonetaryAmount",
      "currency": "USD",
      "value": {
        "@type": "QuantitativeValue",
        "minValue": 65000,
        "maxValue": 84500,
        "unitText": "YEAR"
      }
    },
    "employment_type": [
      "INTERN"
    ],
    "url": "https://www.linkedin.com/jobs/view/civil-engineer-entry-level-at-langan-engineering-environmental-services-4294049665",
    "source_type": "jobboard",
    "source": "linkedin",
    "source_domain": "linkedin.com",
    "organization_logo": "https://media.licdn.com/dms/image/v2/D4E0BAQEo6xLJeEYG2A/company-logo_200_200/company-logo_200_200/0/1707256430119/langan_engineering__environmental_services_inc_logo?e=2147483647&v=beta&t=nNGJ1nq5uG063ORLWn-P0sqDDdbXbz29WYyTgfmLJNI",
    "cities_derived": [
      "Chicago"
    ],
    "counties_derived": [
      "Cook County"
    ],
    "regions_derived": [
      "Illinois"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Chicago, Illinois, United States"
    ],
    "timezones_derived": [
      "America/Chicago"
    ],
    "lats_derived": [
      41.8755616
    ],
    "lngs_derived": [
      -87.6244212
    ],
    "remote_derived": false,
    "recruiter_name": null,
    "recruiter_title": null,
    "recruiter_url": null,
    "linkedin_org_employees": 2139,
    "linkedin_org_url": "http://www.langan.com",
    "linkedin_org_size": "1,001-5,000 employees",
    "linkedin_org_slogan": "Technical Excellence. Practical Experience. Client Responsiveness.",
    "linkedin_org_industry": "Civil Engineering",
    "linkedin_org_followers": 54141,
    "linkedin_org_headquarters": "Parsippany, NJ",
    "linkedin_org_type": "Privately Held",
    "linkedin_org_foundeddate": "1970",
    "linkedin_org_specialties": [
      "Geotechnical",
      "Site/Civil and Environmental Engineering",
      "Transportation/Traffic Engineering",
      "Surveying",
      "3D Laser Scanning",
      "and BIM",
      "Cultural Resources",
      "Natural Resources Assessments/Permitting",
      "Landscape Architecture + Planning",
      "GIS/Data Management Services",
      "PFAS",
      "IWMS",
      "Digital Solutions",
      "and Environmental Compliance"
    ],
    "linkedin_org_locations": [
      "300 Kimball Drive, 4th Floor, Parsippany, NJ 07054, US",
      "368 9th Avenue, 8th Floor, New York, NY 10001, US",
      "1 University Square Drive, Suite 110, Princeton, NJ 08540, US",
      "135 Main Street, Suite 1500, San Francisco, CA 94105, US",
      "One North Broadway, Suite 910, White Plains, NY 10601, US",
      "1818 Market Street, Suite 3300, Philadelphia, PA 19103, US",
      "Long Wharf Maritime Center, 555 Long Wharf Drive, 9th Floor, New Haven, CT 06511, US",
      "100 Cambridge Street Ave, Suite 1310, Boston, Massachusetts 02114, US",
      "2700 Kelly Road, Suite 200, Warrington, PA 18976, US",
      "One West Broad Street, Suite 200, Bethlehem, PA 18018, US",
      "1300 Wilson Boulevard, Suite 450, Arlington, VA 22209, US",
      "1221 Brickell Ave, Suite 1800, Miami, Florida 33131, US",
      "13485 Veterans Way, Suite 120, Orlando, Florida 32827, US",
      "110 E Broward Blvd, Suite 1500, Fort Lauderdale, FL 33301, US",
      "400 N Ashley Dr, Suite 2175, Tampa, FL 33602, US",
      "525 Okeechobee Blvd, Suite 910, West Palm Beach, Florida 33401, US",
      "2400 Ansys Dr, Suite 403, Canonsburg, PA 15317, US",
      "6000 Lombardo Center, Suite 210, Cleveland, OH 44131, US",
      "200 W Madison St, Suite 2900, Chicago, Illinois 60606, US",
      "2555 E Camelback Rd, Suite 510, Phoenix, Arizona 85016, US",
      "840 Gessner Rd, Suite 740, Houston, Texas 77024, US",
      "2999 Olympus Blvd, Suite 165, Dallas, Texas 75019, US",
      "9606 N Mopac Expy, Suite 110, Austin, Texas 78759, US",
      "1101 E SE Loop 323, Suite 101, Tyler, TX 75701, US",
      "3400 Walnut Street, Suite 220, Denver, CO 80205, US",
      "520 Pike St, Suite 985, Seattle, Washington 98101, US",
      "The Boardwalk - 18575 Jamboree Road, Suite 150, Irvine, CA 92612, US",
      "1960 East Grand St, Suite 585, El Segundo, California 90245, US",
      "104 W Anapamu St, Suite 204B, Santa Barbara, California 93101, US",
      "1330 Broadway, Suite 428, Oakland, California 94612, US",
      "1 Almaden Boulevard, Suite 590, San Jose, CA 95113, US",
      "3320 Data Drive, Suite 350, Rancho Cordova, CA 95670, US",
      "Athens Towers, 21st Floor, 2-4, Messogion Avenue, Athens, 115 27, GR",
      "100 4th Avenue SW, Unit 418, Calgary, Alberta T2P 3N2, CA",
      "JAFZA VIEW 18 & 19, 1st Floor, Dubai, PO Box 262746, AE",
      "11-12 Great Sutton Street, 3rd Floor, London, England EC1V 0BX, GB",
      "Avenida Centenario, Office 14A y 14B, P.H Torre Centenario, Panama City, Panama, PA",
      "201 Old Country Rd, #208, Melville, New York 11747, US",
      "333 Commerce St, Suite 1600, Nashville, Tennessee 37201, US",
      "227 W Trade St, Suite 320, Charlotte, North Carolina 28202, US",
      "3600 Lime St, Building 2, Riverside, California 92501, US",
      "257 E 200 S, Suite 410, Salt Lake City, Utah 84111, US",
      "1420 Kettner Boulevard, Suite 100, San Diego, California 92101, US",
      "6671 Las Vegas Blvd S, Building D, Suite 210, Las Vegas, Nevada 89119, US",
      "555 S Preston Rd, Suite 100, Celina, Texas 75009, US",
      "13750 San Pedro Ave, Suite 730, San Antonio, Texas 78232, US",
      "First Central Tower, 360 Central Ave, Suite 800, St Petersburg, Florida 33701, US",
      "247 W Freshwater Way, Suite 530, Milwaukee, Wisconsin 53204, US",
      "1100 New York Ave NW, Suite 210, Washington, District of Columbia 20005, US",
      "224 Harrison St, Suite 210, Office 2, Syracuse, New York 13202, US",
      "Metro Office Park 2, Street 1, San Juan, Puerto Rico 00968, PR"
    ],
    "linkedin_org_description": "Langan's client-focused, highly entrepreneurial culture cultivates an environment of opportunities in which career growth and teamwork flourish. Whether you are a seasoned professional or recent college graduate, Langan will provide you with unparalleled opportunities and a solid foundation for career growth.\n\nOur reputation for providing innovative solutions that yield measurable value for our clients continually forges new enduring relationships for the firm and distinguishes Langan from the competition.\n\nLangan provides an integrated mix of engineering and environmental consulting services in support of land development projects, corporate real estate portfolios, and the energy industry. Our clients include developers, property owners, public agencies, corporations, institutions, and energy companies around the world. \n\nFounded in 1970, Langan employs over 1,900 professionals in its Parsippany, NJ headquarters and among more than 50 regional offices across the country and internationally.\n  ",
    "linkedin_org_recruitment_agency_derived": false,
    "seniority": "Entry level",
    "directapply": false,
    "linkedin_org_slug": "langan-engineering-environmental-services",
    "no_jb_schema": null,
    "external_apply_url": "https://careers.langan.com/job/Chicago-Civil-Engineer-Entry-Level-IL-60606/1296088700/?feedId=359300&utm_source=LinkedInJobPostings",
    "expired": null
  },
  {
    "id": "1862299075",
    "date_posted": "2025-09-02T11:24:23.393",
    "date_created": "2025-09-02T11:36:23.487021",
    "title": "Journalism Intern (Remote)",
    "organization": "Thesocialtalks",
    "organization_url": "https://in.linkedin.com/company/thesocialtalks-com",
    "date_validthrough": null,
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressRegion": "",
          "addressCountry": "",
          "addressLocality": "United Kingdom"
        }
      }
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "INTERN"
    ],
    "url": "https://uk.linkedin.com/jobs/view/journalism-intern-remote-at-thesocialtalks-4294354081",
    "source_type": "jobboard",
    "source": "linkedin",
    "source_domain": "uk.linkedin.com",
    "organization_logo": "https://media.licdn.com/dms/image/v2/D4D0BAQGANCnVbEEpaA/company-logo_100_100/company-logo_100_100/0/1684075359710/thesocialtalks_com_logo?e=2147483647&v=beta&t=wIDjtV7NIJmpRsVPmqHSBT9uMSYw2kDTJC1x0bCPS9w",
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
      54.7023545
    ],
    "lngs_derived": [
      -3.2765753
    ],
    "remote_derived": true,
    "recruiter_name": null,
    "recruiter_title": null,
    "recruiter_url": null,
    "linkedin_org_employees": 93,
    "linkedin_org_url": "https://thesocialtalks.com/",
    "linkedin_org_size": "11-50 employees",
    "linkedin_org_slogan": "A step towards change.",
    "linkedin_org_industry": "Media Production",
    "linkedin_org_followers": null,
    "linkedin_org_headquarters": "New delhi",
    "linkedin_org_type": "Partnership",
    "linkedin_org_foundeddate": "2020",
    "linkedin_org_specialties": [
      ""
    ],
    "linkedin_org_locations": [
      "New delhi, 110002, IN"
    ],
    "linkedin_org_description": "Our Commitment to Ethical and Diverse Journalism\n\nWe offer comprehensive and impartial coverage, exploring a wide spectrum of issues, from local, national, and international news to other important areas. Upholding the highest standards of journalistic integrity, we are committed to freedom of the press and factual reporting. Our approach emphasizes original reporting, online research, and curated information from trusted sources, including expert and official quotes, to ensure accuracy, credibility, and a well-rounded perspective. We bring news and information to the forefront, free from propaganda or hidden agendas, empowering readers to form their own informed opinions.\n\nOur Core Mission\n\nWe are a community-based news media organization that empowers volunteers, professional journalists, editors, citizens, photographers, videographers, fact-checkers, and community managers to report on vital issues and uncover hidden narratives.",
    "linkedin_org_recruitment_agency_derived": false,
    "seniority": "Internship",
    "directapply": true,
    "linkedin_org_slug": "thesocialtalks-com",
    "no_jb_schema": true,
    "external_apply_url": null,
    "expired": null
  },
  {
    "id": "1862301710",
    "date_posted": "2025-09-02T11:24:17",
    "date_created": "2025-09-02T11:39:36.61794",
    "title": "Stage: Online Marketing & Contentcreatie",
    "organization": "Visit Utrecht Region",
    "organization_url": "https://www.linkedin.com/company/visitutrechtregion",
    "date_validthrough": "2025-10-02T11:24:17",
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "NL",
          "addressLocality": "Utrecht",
          "addressRegion": null,
          "streetAddress": null
        },
        "latitude": 52.091682,
        "longitude": 5.120363
      }
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "INTERN"
    ],
    "url": "https://nl.linkedin.com/jobs/view/stage-online-marketing-contentcreatie-at-visit-utrecht-region-4294340681",
    "source_type": "jobboard",
    "source": "linkedin",
    "source_domain": "nl.linkedin.com",
    "organization_logo": "https://media.licdn.com/dms/image/v2/C4E0BAQGWgrU72muTmA/company-logo_200_200/company-logo_200_200/0/1630594264287?e=2147483647&v=beta&t=j-Feht7-RZFSqwWVGYzhMK5-ANYAUzSOCUnBNy2WM88",
    "cities_derived": [
      "Utrecht"
    ],
    "counties_derived": null,
    "regions_derived": [
      "Utrecht"
    ],
    "countries_derived": [
      "Netherlands"
    ],
    "locations_derived": [
      "Utrecht, Utrecht, Netherlands"
    ],
    "timezones_derived": [
      "Europe/Amsterdam"
    ],
    "lats_derived": [
      52.0907006
    ],
    "lngs_derived": [
      5.1215634
    ],
    "remote_derived": false,
    "recruiter_name": null,
    "recruiter_title": null,
    "recruiter_url": null,
    "linkedin_org_employees": 2,
    "linkedin_org_url": "http://www.visitutrechtregion.com",
    "linkedin_org_size": "11-50 employees",
    "linkedin_org_slogan": "Visit Utrecht Region zet de regio Utrecht in de internationale etalage! ",
    "linkedin_org_industry": "Travel Arrangements",
    "linkedin_org_followers": null,
    "linkedin_org_headquarters": "Utrecht",
    "linkedin_org_type": "Nonprofit",
    "linkedin_org_foundeddate": "2016",
    "linkedin_org_specialties": [
      ""
    ],
    "linkedin_org_locations": [
      "Utrecht, NL"
    ],
    "linkedin_org_description": "Visit Utrecht Region is een unieke samenwerking waarbinnen 20 gemeenten, provincie Utrecht en 10 destinatiemarketingorganisaties samenwerken om de regio internationaal op de kaart te zetten. ",
    "linkedin_org_recruitment_agency_derived": false,
    "seniority": "Stagiair",
    "directapply": true,
    "linkedin_org_slug": "visitutrechtregion",
    "no_jb_schema": null,
    "external_apply_url": null,
    "expired": null
  },
  {
    "id": "1862300032",
    "date_posted": "2025-09-02T11:20:46",
    "date_created": "2025-09-02T11:36:53.625018",
    "title": "Technicien(ne) de service interne",
    "organization": "Busch Vacuum Solutions",
    "organization_url": "https://www.linkedin.com/company/busch-vacuum-solutions",
    "date_validthrough": "2025-10-02T11:20:46",
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "CA",
          "addressLocality": "Boisbriand",
          "addressRegion": "QC",
          "streetAddress": null
        },
        "latitude": 45.620102,
        "longitude": -73.85211
      }
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "INTERN"
    ],
    "url": "https://ca.linkedin.com/jobs/view/technicien-ne-de-service-interne-at-busch-vacuum-solutions-4294050591",
    "source_type": "jobboard",
    "source": "linkedin",
    "source_domain": "ca.linkedin.com",
    "organization_logo": "https://media.licdn.com/dms/image/v2/C4E0BAQHmlflecjQf_Q/company-logo_200_200/company-logo_200_200/0/1630620233893/busch_vacuum_solutions_logo?e=2147483647&v=beta&t=zwNcxA-dTCwyOpZe2GkWwT1B5Hxqnrsc8wQEQj6Z-Q0",
    "cities_derived": [
      "Boisbriand"
    ],
    "counties_derived": [
      "Thérèse-De Blainville"
    ],
    "regions_derived": [
      "Quebec"
    ],
    "countries_derived": [
      "Canada"
    ],
    "locations_derived": [
      "Boisbriand, Quebec, Canada"
    ],
    "timezones_derived": [
      "America/Toronto"
    ],
    "lats_derived": [
      45.6130248
    ],
    "lngs_derived": [
      -73.8386113
    ],
    "remote_derived": false,
    "recruiter_name": null,
    "recruiter_title": null,
    "recruiter_url": null,
    "linkedin_org_employees": 2089,
    "linkedin_org_url": "https://www.buschvacuum.com",
    "linkedin_org_size": "1,001-5,000 employees",
    "linkedin_org_slogan": "Intelligent use of vacuum is essential in tackling the challenges of our future.",
    "linkedin_org_industry": "Machinery Manufacturing",
    "linkedin_org_followers": null,
    "linkedin_org_headquarters": "Maulburg",
    "linkedin_org_type": "Privately Held",
    "linkedin_org_foundeddate": "1963",
    "linkedin_org_specialties": [
      "Vacuum pumps",
      "Vacuum systems",
      "Vacuum pump service",
      "Vacuum pump repair",
      "Compressors",
      "Vacuum",
      "Overpressure",
      "Blowers",
      "Centralised vacuum systems",
      "Liquid ring vacuum pumps",
      "industrial vacuum pumps",
      "side channel blower",
      "and rotary vane vacuum pumps"
    ],
    "linkedin_org_locations": [
      "Schauinslandstraße 1, Maulburg, 79689, DE",
      "Hortonwood 30, Telford, Shropshire TF1 7YB, GB",
      "516 Viking Dr, Virginia Beach, VA 23452, US",
      "1740 Boulevard Lionel-Bertrand, Boisbriand, Quebec J7H 1N7, CA",
      "16, Rue du Bois Chaland, Lisses, 91090, FR",
      "Waldweg 22, Magden, 4312, CH",
      "102 – 103, Sector 5, IMT Manesar, Gurugram, Haryana 122 050, IN",
      "Boulevard Díaz Ordaz 260, Col. Santa María, Monterrey, NL 64650, MX",
      "Est. Municipal Santo Gastaldi, 160, Jarinu, São Paulo 13240-000, BR",
      "Pompmolenlaan 2, GK Woerden, 3447, NL",
      "87 Mimetes Road, Denver, Johannesburg, 2094, ZA",
      "Pol. Ind. Coll de la Manya, Carrer Jaume Ferran, 6 - 8, Granollers (Barcelona), 08403, ES",
      "1-23-33, Megumigaoka, Hiratsuka City, Kanagawa 259-1220, JP",
      "Via Ettore Majorana 16, Nova Milanese, MB 20834, IT",
      "Nowa Wieś ul. Dedala, Kruszyn, 787-853, PL",
      "Panamericana 36, Parque Industrial, Guayaquil , 3160, AR",
      "Av. Presidente Eduardo Frei Montalva N° 7070 - 9, Quilicura / Santiago, CL",
      "Av. Calle 24 No. 95-12 Bodega 27, Parque Industrial Portos, Bogotá, CO",
      "Compañía de ventas  Av. Guardia Peruana N° 1050, Chorrillos,  Lima, PE",
      "Businesspark 1, 2100 Korneuburg, AT",
      "Kruinstraat 7, Lokeren, 9160, BE",
      "Vranovská 1551/100, Brno, 614 00, CZ",
      "Parallelvej 11, Ry, 8680 , DK",
      "Sinikellontie 4, Vantaa, 01300 , FI",
      "Gyári út 23, 2310 Szigetszentmiklós, HU",
      "A10-11 Howth Junction Business Centre, Kilbarrack, Dublin 5, D05 X792, IE",
      "A10-11 Howth Junction Business Centre, Kilbarrack, Dublin 5, D05 X792, IE",
      "Holterkollveien 3, Drøbak, 1448 , NO",
      "Travessa da Barrosinha, 84 - Fração B, 3750-753 Travassô, Águeda , PT",
      "Str. Fabricii Nr. 118 A, 400632 Cluj-Napoca, RO",
      "Växthusvägen 2, Mölnlycke, 43533 , SE",
      "Plot # B-154 (Ground Floor)  Road # 22, New D.O.H.S, Mohakhali  Dhaka-1206, BD",
      "上海市闵行区紫星路 1200 号, 邮编: 200241, CN",
      "1st Mevo Sivan Street, Qiryat Gat 8202271, IL",
      "No. 1, Jalan Sungai Jerluh 32 / 196, Seksyen 32, 40460 Shah Alam  Selangor Darul Ehsan, MY",
      "77A Joo Koon Circle, Singapore 629098, SG",
      "189-51, Seoicheon-ro, Majang-myu, Icheon, Gyunggi-do  17385 Republic of Korea, KR",
      "地址:303, 新竹縣湖口鄉成功路1288號, TW",
      "29/10 Moo 7, Soi Poolcharoen,  Bangna-Trad Road, Bangchalong | Bangplee  Samutprakarn 10540, TH",
      "Emlak Kredi Ishani No. 179, 34672 Üsküdar Istanbul, TR",
      "A-3, 71-73 & 75, Sharjah Airport International Free zone (SAIF-Zone), P.B.No: 121855, Sharjah, AE",
      "30 Lakeside Drive, Broadmeadows, Vic.3047, AU",
      "Unit C, 41 Arrenway Drive, Albany, Auckland 0632, NZ"
    ],
    "linkedin_org_description": "The Busch Group is one of the world’s largest manufacturers of vacuum pumps, vacuum systems, blowers, compressors and gas abatement systems. Under its umbrella, the group houses three well-known brands: Busch Vacuum Solutions, Pfeiffer Vacuum and centrotherm clean solutions.\n\nThe extensive product portfolio makes the Busch Group your preferred solution provider for vacuum, overpressure and abatement applications in all industries, such as semiconductors, food, analytics, chemicals and plastics. This also includes the design and construction of tailor-made vacuum systems and the industry’s most extensive worldwide service network.\n\nThe Busch Group is a family business that is managed by the Busch family. More than 8,000 employees in 44 countries worldwide work for the group. Since its beginnings more than 60 years ago, Busch is headquartered in Maulburg, Germany, in the tri-country region of Germany, France and Switzerland.\n\nToday, the Busch Group manufactures in its 23 own production plants in China, the Czech Republic, France, Germany, India, Romania, South Korea, Switzerland, the United Kingdom, the USA and Vietnam, always near to its customers for fast delivery around the globe.\n\nWhat characterizes the family-owned Busch Group is stability, reliability and flexibility. This combination makes us your best one-stop supplier in the vacuum market for innovative, individual solutions.",
    "linkedin_org_recruitment_agency_derived": false,
    "seniority": "Mid-Senior level",
    "directapply": false,
    "linkedin_org_slug": "busch-vacuum-solutions",
    "no_jb_schema": null,
    "external_apply_url": "https://jobs.buschvacuum.com/busch/job/Boisbriand-(QC)-Technicien(ne)-de-service-interne-Québ-J7H1N7/826684402/?utm_source=LINKEDIN&utm_medium=referrer",
    "expired": null
  },
  {
    "id": "1862297819",
    "date_posted": "2025-09-02T11:13:43",
    "date_created": "2025-09-02T11:35:36.860792",
    "title": "Property Management Intern",
    "organization": "Regency Properties",
    "organization_url": "https://www.linkedin.com/company/regency-properties",
    "date_validthrough": "2025-09-19T23:15:09",
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "US",
          "addressLocality": "Evansville",
          "addressRegion": "IN",
          "streetAddress": null
        },
        "latitude": 37.97676,
        "longitude": -87.48122
      }
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "INTERN"
    ],
    "url": "https://www.linkedin.com/jobs/view/property-management-intern-at-regency-properties-4294349215",
    "source_type": "jobboard",
    "source": "linkedin",
    "source_domain": "linkedin.com",
    "organization_logo": "https://media.licdn.com/dms/image/v2/C4E0BAQGi9QTinxHdKQ/company-logo_200_200/company-logo_200_200/0/1630578734552/regency_properties_logo?e=2147483647&v=beta&t=l6QGk7FAVINXPA6Z3CoKU5Odr9wv9inUG_YODd1g9c4",
    "cities_derived": [
      "Evansville"
    ],
    "counties_derived": [
      "Vanderburgh County"
    ],
    "regions_derived": [
      "Indiana"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Evansville, Indiana, United States"
    ],
    "timezones_derived": [
      "America/Chicago"
    ],
    "lats_derived": [
      37.970495
    ],
    "lngs_derived": [
      -87.5715641
    ],
    "remote_derived": false,
    "recruiter_name": null,
    "recruiter_title": null,
    "recruiter_url": null,
    "linkedin_org_employees": 52,
    "linkedin_org_url": "https://regency-prop.com",
    "linkedin_org_size": "11-50 employees",
    "linkedin_org_slogan": "Specializing in County Seat Communities",
    "linkedin_org_industry": "Leasing Non-residential Real Estate",
    "linkedin_org_followers": 782,
    "linkedin_org_headquarters": "Evansville, IN",
    "linkedin_org_type": "Privately Held",
    "linkedin_org_foundeddate": "1949",
    "linkedin_org_specialties": [
      "Property Development",
      "Redevelopment",
      "Acquisitions",
      "Sales",
      "Leasing",
      "Real Estate",
      "Retail Real Estate",
      "County Seat Communities",
      "Retailers",
      "and Essential businesses"
    ],
    "linkedin_org_locations": [
      "380 N. Cross Pointe Blvd, Evansville, IN 47715, US"
    ],
    "linkedin_org_description": "Regency Properties’ primary expertise is ownership and management of shopping centers in “county seat communities.” A winner of “Best in Industry for Commercial Real Estate Customer Service,” Regency Properties is committed to the success of every tenant. ",
    "linkedin_org_recruitment_agency_derived": false,
    "seniority": "Internship",
    "directapply": false,
    "linkedin_org_slug": "regency-properties",
    "no_jb_schema": null,
    "external_apply_url": "https://regencyprop.exacthire.com/job/174382?source=361",
    "expired": null
  },
  {
    "id": "1862297816",
    "date_posted": "2025-09-02T11:13:37",
    "date_created": "2025-09-02T11:35:36.782625",
    "title": "Social Media Marketing Intern",
    "organization": "Stéphen House Creative",
    "organization_url": "https://www.linkedin.com/company/st%C3%A9phen-house-creative",
    "date_validthrough": "2025-10-02T11:13:37",
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "US",
          "addressLocality": "Georgia",
          "addressRegion": "United States",
          "streetAddress": null
        },
        "latitude": 32.64829,
        "longitude": -83.444374
      }
    ],
    "location_type": "TELECOMMUTE",
    "location_requirements_raw": [
      {
        "@type": "Country",
        "name": "Georgia, United States"
      }
    ],
    "salary_raw": null,
    "employment_type": [
      "INTERN"
    ],
    "url": "https://www.linkedin.com/jobs/view/social-media-marketing-intern-at-st%C3%A9phen-house-creative-4294340543",
    "source_type": "jobboard",
    "source": "linkedin",
    "source_domain": "linkedin.com",
    "organization_logo": "https://media.licdn.com/dms/image/v2/D4E0BAQEC1X7iDEkPcQ/company-logo_200_200/B4EZhbQWGtHEAI-/0/1753877668606?e=2147483647&v=beta&t=Q9XoMfV8WPXwuqpv3daen1XT5XHkFz_L_uoSW8rY7Fs",
    "cities_derived": null,
    "counties_derived": null,
    "regions_derived": [
      "Georgia"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Georgia, United States"
    ],
    "timezones_derived": [
      "America/New_York"
    ],
    "lats_derived": [
      32.3293809
    ],
    "lngs_derived": [
      -83.1137366
    ],
    "remote_derived": true,
    "recruiter_name": null,
    "recruiter_title": null,
    "recruiter_url": null,
    "linkedin_org_employees": 1,
    "linkedin_org_url": "http://stephenhousecreative.org/",
    "linkedin_org_size": "1 employee",
    "linkedin_org_slogan": "Stylish Nursery Essentials for Modern Parents",
    "linkedin_org_industry": "Retail",
    "linkedin_org_followers": 34,
    "linkedin_org_headquarters": "Tyrone, GA",
    "linkedin_org_type": "Privately Held",
    "linkedin_org_foundeddate": "2023",
    "linkedin_org_specialties": [
      ""
    ],
    "linkedin_org_locations": [
      "Tyrone, GA 30290, US"
    ],
    "linkedin_org_description": "Stéphen House Creative is a modern, family-focused lifestyle brand dedicated to creating thoughtful, sophisticated solutions for parents and children. Founded by a mom with a passion for intentional living, we combine style, functionality, and sustainability to inspire families and support them in every stage of early parenthood.\n\nAt Stéphen House Creative, we believe in designing experiences, resources, and products that celebrate connection, nurture creativity, and foster healthy development for children. Our mission is to empower parents and caregivers to provide intentional, stylish, and sustainable environments for their families.\n\nWe specialize in collaborations and partnerships with professionals across the parenting and children’s wellness ecosystem—including birth doulas, pediatric sleep consultants, potty training coaches, RNs, and early childhood educators. By working together, we aim to deliver meaningful, expert-backed solutions that make family life more manageable, elegant, and joyful.\n\nOur approach prioritizes safety, quality, and timeless design. From eco-conscious nursery essentials to thoughtfully curated gift sets for families, every creation embodies our commitment to premium children’s lifestyle products. We offer unique opportunities for co-branding, educational content collaborations, and expert-informed partnerships that connect directly with parents seeking modern, family-first solutions.\n\nIf you are a children’s brand, parenting consultant, or family-focused professional interested in collaboration, co-marketing, or creative partnership, Stéphen House Creative welcomes the opportunity to connect. Together, we can inspire families, elevate parenting experiences, and promote sustainable, intentional living for the next generation.",
    "linkedin_org_recruitment_agency_derived": false,
    "seniority": "Not Applicable",
    "directapply": true,
    "linkedin_org_slug": "st%C3%A9phen-house-creative",
    "no_jb_schema": null,
    "external_apply_url": null,
    "expired": null
  },
  {
    "id": "1862302066",
    "date_posted": "2025-09-02T11:13:12",
    "date_created": "2025-09-02T11:40:14.47817",
    "title": "Internship | Beamforming Strategies for Joint Communication and Sensing (JCAS) Services in 6G Networks",
    "organization": "TNO",
    "organization_url": "https://www.linkedin.com/company/tno",
    "date_validthrough": "2026-03-16T16:48:02",
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "NL",
          "addressLocality": "Den Haag",
          "addressRegion": null,
          "streetAddress": null
        },
        "latitude": 52.080196,
        "longitude": 4.3101325
      }
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "INTERN"
    ],
    "url": "https://nl.linkedin.com/jobs/view/internship-beamforming-strategies-for-joint-communication-and-sensing-jcas-services-in-6g-networks-at-tno-3911267545",
    "source_type": "jobboard",
    "source": "linkedin",
    "source_domain": "nl.linkedin.com",
    "organization_logo": "https://media.licdn.com/dms/image/v2/D560BAQFpzeRcB1ORjQ/company-logo_200_200/B56ZfEqi2yHUAQ-/0/1751351177031/tno_logo?e=2147483647&v=beta&t=iDhScTl0sMsGJ0KszSsziikGSgItcb21J9HhT9hhLw8",
    "cities_derived": [
      "The Hague"
    ],
    "counties_derived": null,
    "regions_derived": [
      "South Holland"
    ],
    "countries_derived": [
      "Netherlands"
    ],
    "locations_derived": [
      "The Hague, South Holland, Netherlands"
    ],
    "timezones_derived": [
      "Europe/Amsterdam"
    ],
    "lats_derived": [
      52.0799838
    ],
    "lngs_derived": [
      4.3113461
    ],
    "remote_derived": false,
    "recruiter_name": null,
    "recruiter_title": null,
    "recruiter_url": null,
    "linkedin_org_employees": 5596,
    "linkedin_org_url": "http://www.tno.nl/en",
    "linkedin_org_size": "1,001-5,000 employees",
    "linkedin_org_slogan": "Wij zijn de onafhankelijke innovatie, onderzoeks- en adviesorganisatie voor bedrijven en overheden. #ditisonzetijd",
    "linkedin_org_industry": "Research Services",
    "linkedin_org_followers": null,
    "linkedin_org_headquarters": "2595 DA The Hague",
    "linkedin_org_type": "Nonprofit",
    "linkedin_org_foundeddate": "1932",
    "linkedin_org_specialties": [
      "Public safety",
      "Defence",
      "Safety and Security",
      "Healthy living",
      "Food",
      "Dealing with changing society",
      "Accessibility",
      "Living with water",
      "Energy (management)",
      "High-tech systems processes & materials",
      "Industrial Innovation",
      "Built Environment",
      "Mobility",
      "Information Society",
      "and CO2reduction"
    ],
    "linkedin_org_locations": [
      "New Babylon, Anna van Buerenplein 1, 2595 DA The Hague, NL",
      "Utrechtseweg 48, Zeist, Utrecht 3704 HK, NL",
      "Radarweg 60, Amsterdam, North Holland 1043 NT, NL",
      "Auvergnedijk 2, Bergen op Zoom, North Brabant 4612 PZ, NL",
      "Aarlenstraat 22, Brussels, Brussels Region B-1050, BE",
      "Leeghwaterstraat 44, Delft, 2628 CA, NL"
    ],
    "linkedin_org_description": "TNO is an independent organisation for applied research. We connect people and knowledge to create innovations that boost the competitive strength of industry and the well-being of society in a sustainable way. Our goal is to connect, change and accelerate: Innovation for life.",
    "linkedin_org_recruitment_agency_derived": false,
    "seniority": "Stagiair",
    "directapply": false,
    "linkedin_org_slug": "tno",
    "no_jb_schema": null,
    "external_apply_url": "https://www.tno.nl/en/careers/vacancies/2024/04/internship-beamforming-strategies-joint/",
    "expired": null
  },
  {
    "id": "1862298246",
    "date_posted": "2025-09-02T11:12:34",
    "date_created": "2025-09-02T11:35:52.459353",
    "title": "Thermal Process Engineering Intern - Summer 2026",
    "organization": "Corning Incorporated",
    "organization_url": "https://www.linkedin.com/company/corning-incorporated",
    "date_validthrough": "2025-10-02T11:12:33",
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "US",
          "addressLocality": "Painted Post",
          "addressRegion": "NY",
          "streetAddress": null
        },
        "latitude": 42.154797,
        "longitude": -77.11912
      }
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "INTERN"
    ],
    "url": "https://www.linkedin.com/jobs/view/thermal-process-engineering-intern-summer-2026-at-corning-incorporated-4292765048",
    "source_type": "jobboard",
    "source": "linkedin",
    "source_domain": "linkedin.com",
    "organization_logo": "https://media.licdn.com/dms/image/v2/D4E0BAQFZTU7aq2D19Q/company-logo_200_200/B4EZXSZA1cHMAM-/0/1742991527677/corning_incorporated_logo?e=2147483647&v=beta&t=uVERgJ8d4ylwf8ncs9gICaLo-8GYsACP2GCcok0xQ4Q",
    "cities_derived": [
      "Painted Post"
    ],
    "counties_derived": [
      "Steuben County"
    ],
    "regions_derived": [
      "New York"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Painted Post, New York, United States"
    ],
    "timezones_derived": [
      "America/New_York"
    ],
    "lats_derived": [
      42.1620186
    ],
    "lngs_derived": [
      -77.0941366
    ],
    "remote_derived": false,
    "recruiter_name": null,
    "recruiter_title": null,
    "recruiter_url": null,
    "linkedin_org_employees": 20392,
    "linkedin_org_url": "https://www.corning.com",
    "linkedin_org_size": "10,001+ employees",
    "linkedin_org_slogan": null,
    "linkedin_org_industry": "Glass, Ceramics and Concrete Manufacturing",
    "linkedin_org_followers": 217187,
    "linkedin_org_headquarters": "Corning, New York",
    "linkedin_org_type": "Public Company",
    "linkedin_org_foundeddate": "",
    "linkedin_org_specialties": [
      "Display Technologies",
      "Environmental Technologies",
      "Telecommunications",
      "and Life Sciences & Specialty Materials"
    ],
    "linkedin_org_locations": [
      "One Riverfront Plaza, Corning, New York 14831, US",
      "One Riverfront Plaza, Corning, New York 14831, US"
    ],
    "linkedin_org_description": "Corning is one of the world's leading innovators in materials science, with a 170+ year track record of life-changing inventions. Corning applies its unparalleled expertise in glass science, ceramics science, and optical physics along with its deep manufacturing and engineering capabilities to develop category-defining products that transform industries and enhance people's lives. Corning succeeds through sustained investment in RD&E, a unique combination of material and process innovation, and deep, trust-based relationships with customers who are global leaders in their industries. \n\nCorning's capabilities are versatile and synergistic, which allows the company to evolve to meet changing market needs, while also helping our customers capture new opportunities in dynamic industries. Today, Corning's markets include optical communications, mobile consumer electronics, display technology, automotive, and life sciences vessels. Corning's industry-leading products include damage-resistant cover glass for mobile devices; precision glass for advanced displays; optical fiber, wireless technologies, and connectivity solutions for state-of-the-art communications networks; trusted products to accelerate drug discovery and delivery; and clean-air technologies for cars and trucks.\n\nTerms of Use: http://ow.ly/ObPiI",
    "linkedin_org_recruitment_agency_derived": false,
    "seniority": "Internship",
    "directapply": false,
    "linkedin_org_slug": "corning-incorporated",
    "no_jb_schema": null,
    "external_apply_url": "https://corningjobs.corning.com/job/Painted-Post-Thermal-Process-Engineering-Intern-Summer-2026-NY-14870/1321630100/?utm_source=LINKEDIN&utm_medium=referrer",
    "expired": null
  },
  {
    "id": "1862297507",
    "date_posted": "2025-09-02T11:12:33",
    "date_created": "2025-09-02T11:35:25.072783",
    "title": "Operations Intern - Summer 2026",
    "organization": "Corning Incorporated",
    "organization_url": "https://www.linkedin.com/company/corning-incorporated",
    "date_validthrough": "2025-10-02T11:12:33",
    "locations_raw": [
      {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "US",
          "addressLocality": "Winston-Salem",
          "addressRegion": "NC",
          "streetAddress": null
        },
        "latitude": 36.050026,
        "longitude": -80.18339
      }
    ],
    "location_type": null,
    "location_requirements_raw": null,
    "salary_raw": null,
    "employment_type": [
      "INTERN"
    ],
    "url": "https://www.linkedin.com/jobs/view/operations-intern-summer-2026-at-corning-incorporated-4292753948",
    "source_type": "jobboard",
    "source": "linkedin",
    "source_domain": "linkedin.com",
    "organization_logo": "https://media.licdn.com/dms/image/v2/D4E0BAQFZTU7aq2D19Q/company-logo_200_200/B4EZXSZA1cHMAM-/0/1742991527677/corning_incorporated_logo?e=2147483647&v=beta&t=uVERgJ8d4ylwf8ncs9gICaLo-8GYsACP2GCcok0xQ4Q",
    "cities_derived": [
      "Winston-Salem"
    ],
    "counties_derived": [
      "Forsyth County"
    ],
    "regions_derived": [
      "North Carolina"
    ],
    "countries_derived": [
      "United States"
    ],
    "locations_derived": [
      "Winston-Salem, North Carolina, United States"
    ],
    "timezones_derived": [
      "America/New_York"
    ],
    "lats_derived": [
      36.0998131
    ],
    "lngs_derived": [
      -80.2440518
    ],
    "remote_derived": false,
    "recruiter_name": null,
    "recruiter_title": null,
    "recruiter_url": null,
    "linkedin_org_employees": 20392,
    "linkedin_org_url": "https://www.corning.com",
    "linkedin_org_size": "10,001+ employees",
    "linkedin_org_slogan": null,
    "linkedin_org_industry": "Glass, Ceramics and Concrete Manufacturing",
    "linkedin_org_followers": 217187,
    "linkedin_org_headquarters": "Corning, New York",
    "linkedin_org_type": "Public Company",
    "linkedin_org_foundeddate": "",
    "linkedin_org_specialties": [
      "Display Technologies",
      "Environmental Technologies",
      "Telecommunications",
      "and Life Sciences & Specialty Materials"
    ],
    "linkedin_org_locations": [
      "One Riverfront Plaza, Corning, New York 14831, US",
      "One Riverfront Plaza, Corning, New York 14831, US"
    ],
    "linkedin_org_description": "Corning is one of the world's leading innovators in materials science, with a 170+ year track record of life-changing inventions. Corning applies its unparalleled expertise in glass science, ceramics science, and optical physics along with its deep manufacturing and engineering capabilities to develop category-defining products that transform industries and enhance people's lives. Corning succeeds through sustained investment in RD&E, a unique combination of material and process innovation, and deep, trust-based relationships with customers who are global leaders in their industries. \n\nCorning's capabilities are versatile and synergistic, which allows the company to evolve to meet changing market needs, while also helping our customers capture new opportunities in dynamic industries. Today, Corning's markets include optical communications, mobile consumer electronics, display technology, automotive, and life sciences vessels. Corning's industry-leading products include damage-resistant cover glass for mobile devices; precision glass for advanced displays; optical fiber, wireless technologies, and connectivity solutions for state-of-the-art communications networks; trusted products to accelerate drug discovery and delivery; and clean-air technologies for cars and trucks.\n\nTerms of Use: http://ow.ly/ObPiI",
    "linkedin_org_recruitment_agency_derived": false,
    "seniority": "Internship",
    "directapply": false,
    "linkedin_org_slug": "corning-incorporated",
    "no_jb_schema": null,
    "external_apply_url": "https://corningjobs.corning.com/job/Winston-Salem-Operations-Intern-Summer-2026-NC-27107/1321542700/?utm_source=LINKEDIN&utm_medium=referrer",
    "expired": null
  }
]