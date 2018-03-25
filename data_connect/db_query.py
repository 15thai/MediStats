

def sql_providers_in_zip(zip_code = 22901):
    query = """
    WITH tmp_df as (

    SELECT 
     "First Name of the Provider"||' '||"Last Name/Organization Name of the Provider"||', '||"Credentials of the Provider" as name,
     "Street Address 1 of the Provider"|| as street
     "City of the Provider"||', '||"State Code of the Provider" ||' '||substring("Zip Code of the Provider" from 1 for 5) as address,
     "Number of Services" as num_services
    FROM providers
    JOIN puf_hcpcs_agg ON providers."National Provider Identifier" = puf_hcpcs_agg."National Provider Identifier"
    WHERE substring("Zip Code of the Provider" from 1 for 5) = '{}'
    )

    SELECT 
        name, street, address,
        sum(num_services) as num_procedures
    FROM tmp_df
    GROUP BY 
        name, street, address
    """.format(zip_code)
    return query