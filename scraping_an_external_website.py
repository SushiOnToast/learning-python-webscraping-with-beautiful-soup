from bs4 import BeautifulSoup
import requests
import time

# print("Put some skills that you are not familiar with")
# unfamiliar_skills = input('>>').replace(" ", "").split(",")
# print(f"Filtering out {', '.join(unfamiliar_skills)}")

def find_jobs():
    html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all(class_='srp-listing')

    for index, job in enumerate(jobs):
        job_heading = job.find(class_='srp-job-heading')
        posting_time = job_heading.find(class_='posting-time').text
        post_filter = posting_time.split()[0]
        
        if int(post_filter) <= 3:
            job_title = job_heading.find('h3').text
            company_name = job_heading.find(class_='srp-comp-name').text

            skills = job.find(class_='srp-keyskills').find_all('a')
            skill_list = [skill.text for skill in skills]

            more_info = job.find('a')['href']
            
            # has_unfamiliar_skill = any(skill.lower() in skill_list for skill in unfamiliar_skills)
            
            # if not has_unfamiliar_skill:
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Job title: {job_title.strip()} \n")
                f.write(f"Company name: {company_name.strip()} \n")
                f.write(f"Required skills: {', '.join(skill_list)} \n")
                f.write(f"More info: {more_info} \n")

if __name__ == "__main__":
    while True:
        find_jobs()
        print("waiting...")
        time.sleep(600)