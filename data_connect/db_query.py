

def sql_providers_in_zip(zip_code = 22901):
    query = """
    SELECT *
    FROM providers
    WHERE substring("Zip Code of the Provider" from 1 for 5) = '{}'
    """.format(zip_code)
    return query