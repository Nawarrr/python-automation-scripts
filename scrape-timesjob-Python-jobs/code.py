from bs4 import BeautifulSoup
import requests
import time


def unfamiler_skills():
    '''
    This Function takes input from the user to filter out the skills that the user isn't familiar with
    '''
    x = input("Do you want to filter out a skill? y / n  ")
    unfamiler_skills = []
    while x == "y" :
        unfamiler_skill = input("Write skill You are not familiar with to filter the jobs : ")
        unfamiler_skills.append(unfamiler_skill)
        x = input("Do you want to add more skills ? y / n  ")
    return unfamiler_skills



def find_jobs():
    '''
    This function scrapes the website for jobs
    '''
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li' , class_='clearfix job-bx wht-shd-bx')
    return jobs

def save_jobs(jobs , location):
    '''
    This function filters and saves the jobs in a file entered as input
    '''
    with open( location , 'w') as file :
        for job in jobs :
            post_time = job.find("span" , class_ ="sim-posted").text.strip()
            if post_time == "Posted few days ago":
                company_name = job.find("h3" , class_ = "joblist-comp-name").text.strip()
                skills = job.find('span' , class_="srp-skills").text.strip()
                job_link = job.header.h2.a['href']
                final_job = f'Company Name :{company_name}\nRequired Skills : {skills}\nMore Info : {job_link}\n'

                if all(x not in skills.lower() for x in unfamiler_skills )  or len(unfamiler_skills) == 0:
                    file.write(final_job + "\n")



if __name__ == '__main__':
    while True :
        unfamiler_skills = unfamiler_skills()
        jobs = find_jobs()
        save_jobs(jobs, 'jobs.txt')
        print("Waiting for the next run")
        time.sleep(60*60)