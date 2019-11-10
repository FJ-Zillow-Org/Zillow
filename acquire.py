import pandas as pd
import env

# def get_connection(db, user=env.user, host=env.host, password=env.password):
#     return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# Remove any properties that are likely to be something other than a single unit properties (e.g. no duplexes, no land/lot, ...). There are multiple ways to estimate that a property is a single unit, and there is not a single "right" answer.


def get_db_url(db, user= env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_zillow_data():
    query = '''
    select 
    p.`taxamount`/p.`taxvaluedollarcnt` tax_rate,
	p.`bathroomcnt`,
    p.`bedroomcnt`,
    p.`calculatedfinishedsquarefeet`,
    p.`fips`,
    p.`garagecarcnt`,
    p.`garagetotalsqft`,
    p.`latitude`,
    p.`longitude`,
    p.`lotsizesquarefeet`,
    p.`poolcnt`,
    p.`poolsizesum`,
    p.`taxvaluedollarcnt`,
    p.`yearbuilt`,
    p.`landtaxvaluedollarcnt`,
    p.`taxdelinquencyflag`,
    p.`taxdelinquencyyear`, 
    pred.`logerror`,
    m.`transactions`
    from 
	`properties_2017` p
    inner join `predictions_2017`  pred
    on p.`parcelid` = pred.`parcelid` 
    inner join 
	(select 
		`parcelid`, 
		max(`transactiondate`) `lasttransactiondate`, 
		max(`id`) `maxid`, 
		count(*) `transactions`
	from 
		predictions_2017
	group by 
		`parcelid`
	) m
	on 
	pred.parcelid = m.parcelid
	and pred.transactiondate = m.lasttransactiondate
    left join `propertylandusetype` plut
        on p.`propertylandusetypeid` = plut.`propertylandusetypeid`
            
    left join `airconditioningtype` act
        using(`airconditioningtypeid`)
    left join heatingorsystemtype hst
        using(`heatingorsystemtypeid`)
    left join `architecturalstyletype` ast
        using(`architecturalstyletypeid`)
    left join `buildingclasstype` bct
        using(`buildingclasstypeid`)
    left join `storytype` st
        using(`storytypeid`)
    left join `typeconstructiontype` tct
        using(`typeconstructiontypeid`)
    where 
        p.`latitude` is not null
        and p.`longitude` is not null
        and p.bedroomcnt > 0 and p.bathroomcnt > 0
        and plut.propertylandusetypeid = '261';
    '''

    df = pd.read_sql(query, get_db_url('zillow'))
    return df