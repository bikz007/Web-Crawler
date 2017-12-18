import os

#EACH WEBSITE YOU CRAWL IS SEPARATE PROJECT(FOLDER)

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project'+ directory)
        os.makedirs(directory)


#FILES that are gonna be inside directory are queue and crawled files

#CReate queue and crawled files
def create_data_files(project_name,base_url):
    queue=project_name+"/queue.txt"
    crawled=project_name+"/crawled.txt"
    if not os.path.isfile(queue):     #does this file exists already
        write_file(queue,base_url)

    if not os.path.isfile(crawled):
        write_file(crawled,"")




#Create new file
def write_file(path,data):
    f=open(path,'w')
    f.write(data)
    f.close()

#Add data onto an existing file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')


#Delete the contents of File
def delete_file_contents(path):
    with open(path,'w'):
        pass


#read a file and convert  each line  to set items
def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f:      #rt stands for read text
        for line in f:
            results.add(line.replace('\n',''))
    return  results


#Iterate through a set and each item will be a new line in the file
def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)


