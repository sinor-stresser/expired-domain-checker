### made by https://emailnightmare.com
import whois
import time

def check_domain_expiry(domain):
    try:
        domain_info = whois.whois(domain)
        expiry_date = domain_info.expiration_date
        
        if isinstance(expiry_date, list):
            expiry_date = expiry_date[0]
        
        if expiry_date:
            return f"{domain} - Expires on: {expiry_date}"
        else:
            return f"{domain} - Expiry date not found"
    except Exception as e:
        return f"{domain} - Error: {e}"

def main():
    print("Made by https://emailnightmare.com")
    with open("domains.txt", "r") as file:
        domains = [line.strip() for line in file.readlines()]
    
    with open("done.txt", "w") as output_file:
        for domain in domains:
            result = check_domain_expiry(domain)
            print(result)
            output_file.write(result + "\n")
            time.sleep(4)  # Wait 4 seconds before the next check

if __name__ == "__main__":
    main()
