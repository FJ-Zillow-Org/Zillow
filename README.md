# Zillow Project
This is our first partner project using an organization to coordinate on Github. 

## What variables contribute to the logerror of Zillow's Zestimates?

## Audience: Our Data Science Class
- We will use our Jupyter Notebook to do a walkthrough of our process and findings.
## Goals:
- Build a model that can predict the target, continuous variable, of logerror.
- Find any patterns that may be in the residuals.
## Requirements:
- Use clustering in one or more stages of the process.
- Discuss highlights or discoveries from the data, from the project, and from data science.
- Creates .py modules that hold any functions you use throughout the project.
## Deliverables:
- Jupyter Notebook
- Supporting Modules with functions
## Want to run this yourself? You need...
- zillow data csv file in our repo
- a env.py file with host, user, and password
## To recreate this project...
- Pull all .py files
    - acquire.py
    - prepare.py
    - summarize.py
- Add your own env.py file
- Run through deliverable.ipynb

## Data Dictionary

- tax_rate                        float64

    - calculated column using taxamount/taxvaluedollarcnt
    
- bathroomcnt                     float64

    - number of full and half baths
    
- bedroomcnt                      float64

    - number of bedrooms

- calculatedfinishedsquarefeet    float64

    - square footage of entire home

- fips                            float64

    - county codes
 https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697

- garagecarcnt                    float64

    - number of car garage (34203 missing values in original df)

- latitude                        float64

    - latitude divided by 1 million

- longitude                       float64

    - longitude divided by 1 million

- lotsizesquarefeet               float64

    - size of lot in square feet

- poolcnt                         float64

    - number of pools (41105 missing values in original df)

- taxvaluedollarcnt               float64

    - home value in US dollars

- yearbuilt                       float64

    - year the home was built (1878 - 2015)

- landtaxvaluedollarcnt           float64

    - land value in US dollars

- logerror                        float64

    - the difference between the Zestimate and the actual sales price (our target variable)

- county_name                     object

    - Los Angeles, Orange, Ventura counties derived from fips codes

- price_per_sq_ft                 float64

    - calculated column using taxvaluedollarcnt / calculatedfinishedsquareft

- lot_price_per_sq_ft             float64

    - calculated columns using landtaxvaluedollarcnt / lotsizesquarefeet

- los_angeles                     float64

    - binned column with 1 indicating a home in Los Angeles county, 0 if not

- ventura                         float64

    - binned column with 1 indicating a home in Ventura county, 0 if not

- orange                          float64

    - - binned column with 1 indicating a home in Orange county, 0 if not