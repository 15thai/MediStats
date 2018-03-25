

def sql_providers_in_zip(zip_code = 22901):
    query = """
    SELECT *
    FROM providers
    WHERE zipcode = {}

    """.format(zip_code)
    return query