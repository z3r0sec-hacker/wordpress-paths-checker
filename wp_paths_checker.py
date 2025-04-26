import requests
import argparse

banner = r'''
 ______     ______     ______     ______     ______     ______     ______    
/\  ___\   /\  __ \   /\  == \   /\  ___\   /\  ___\   /\  == \   /\  __ \   
\ \___  \  \ \ \/\ \  \ \  __<   \ \  __\   \ \  __\   \ \  __<   \ \ \/\ \  
 \/\_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\ 
  \/_____/   \/_____/   \/_/ /_/   \/_____/   \/_____/   \/_/ /_/   \/_____/ 
                                                                            
'''

print(banner)
print("\nWelcome to z3r0sec WordPress Sensitive Paths Checker!\n")

# Parse arguments
parser = argparse.ArgumentParser(description="WordPress Sensitive Paths Checker by z3r0sec")
parser.add_argument("-u", "--url", required=True, help="Target URL (e.g., http://example.com)")
args = parser.parse_args()

target = args.url

# WordPress common sensitive paths
paths = [
    "/wp-admin/",
    "/wp-login.php",
    "/wp-config.php",
    "/wp-content/",
    "/wp-includes/",
    "/wp-cron.php",
    "/wp-json/",
    "/wp-login.php",
    "/xmlrpc.php",
    "/wp-settings.php",
    "/wp-comments-post.php",
    "/wp-trackback.php",
    "/readme.html",
    "/license.txt",
    "/wp-content/plugins/",
    "/wp-content/themes/",
    "/wp-content/uploads/",
    "/wp-includes/css/",
    "/wp-includes/js/",
    "/wp-includes/images/",
    "/wp-admin/includes/",
    "/wp-content/mu-plugins/",
    "/wp-content/cache/",
    "/wp-content/backups/",
    "/wp-content/uploads/wpforo/",
    "/wp-content/uploads/plugins/",
    "/wp-content/uploads/themes/",
    "/wp-content/uploads/2023/",
    "/wp-content/uploads/2022/",
    "/wp-content/uploads/2021/",
    "/wp-content/uploads/2020/",
    "/wp-content/uploads/2019/",
    "/wp-content/uploads/2018/",
    "/wp-content/uploads/2017/",
    "/wp-content/uploads/2016/",
    "/wp-content/uploads/2015/",
    "/wp-content/uploads/2014/",
    "/wp-content/uploads/2013/",
    "/wp-content/uploads/2012/",
    "/wp-content/uploads/2011/",
]

print(f"\n[+] Scanning target: {target}\n")

for path in paths:
    url = f"{target.rstrip('/')}/{path.lstrip('/')}"  # remove slashes if needed
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"[FOUND] {url} (Status: 200)")
        elif response.status_code in [301, 302]:
            print(f"[REDIRECT] {url} (Status: {response.status_code})")
        elif response.status_code == 403:
            print(f"[FORBIDDEN] {url} (Status: 403)")
        else:
            pass  # Uncomment to show all statuses
            # print(f"[INFO] {url} (Status: {response.status_code})")
    except requests.exceptions.RequestException:
        print(f"[ERROR] Failed to connect to {url}")
