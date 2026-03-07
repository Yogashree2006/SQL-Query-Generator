dangerous_keywords = [
    "DROP", "DELETE", "ALTER", "TRUNCATE",
    "INSERT", "UPDATE", "EXEC", "EXECUTE"
]

dangerous_patterns = [";", "--", "/*", "*/"]

def is_safe(query):
    query_upper = query.upper()
    
    for word in dangerous_keywords:
        if word in query_upper:
            return False
    
    for pattern in dangerous_patterns:
        if pattern in query:
            return False
    
    return True