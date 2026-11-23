#make application to download TEXT BASED SOCIAL MEDIA
#grab all code from text based social media and zip it
local_dir = "./Home/Games/Cookie"
repo_url = "https://github.com/Xylin-Holstein/cookie.git"
print("Welcome to The Store\nNot much to do here")
d = input("Which program would you like to download?\n\nCookie\n")
if d ==("Cookie"):
  print("Please Wait...")
  if local_dir:
    command = f"git clone {repo_url} {local_dir}"
  else:
    command = f"git clone {repo_url}"

  return_code = os.system(command)
  if return_code == 0:
    print("Repository cloned successfully.")
  else:
    print(f"Error cloning repository. Return code: {return_code}")