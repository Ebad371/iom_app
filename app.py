import pandas as pd 
import streamlit as st 
import random
from streamlit_option_menu import option_menu

import pandas as pd
import numpy as np
import random

data = {'jobs': ['Data Scientist',
  'HR',
  'ML Engineer',
  'SEO',
  'Content Writer',
  'Data Engineer',
  'Senior Data Scientist',
  'Android Developer',
  'MERN Stack Developer',
  'Marketing Specialist'],
 'job_addresses': ['Seattle',
  'Los Angeles',
  'Miami',
  'London',
  'Seattle',
  'Atlanta',
  'Berlin',
  'New York',
  'Warsaw',
  'New Jersey'],
 'candidate_names': ['Ebad',
  'David',
  'Andrew',
  'Alex',
  'Melissa',
  'Kate',
  'Sara',
  'John',
  'Lisa',
  'Mohammad'],
 'candidate_skills': ['data science;problem solving;analysis;python',
  'microsoft office;communication;data-driven decisions;entrepreneurship;organizational skills',
  'programming;java;problem solving;android;ios;mobile development',
  'data extraction;etl;data warehouse;mathematics',
  'content writing;creativity;content understanding;organizational skills',
  'problem solving;data analytics;clustering;algorithms;machine learning;optimization',
  'machine learning;deep learning;algorithms;mathematics;keras;azure;tensorflow',
  'social media;facebook;twitter;engagement;comprehensiveness;team building',
  'google search;seo',
  'MongoDB;NodeJS;Express;React'],
 'candidates': {'Ebad': [['Data Scientist', 'Data Engineer', 'SEO', 'HR'],
   [0.3394664772663317, 0.14156576967603743, 0.07091927237638739, 0.0]],
  'David': [['HR', 'Data Scientist', 'Data Engineer', 'Content Writer'],
   [0.44539723121318653,
    0.15722856214570313,
    0.06556813089308454,
    0.0514383040706968]],
  'Andrew': [['Android Developer', 'ML Engineer', 'Data Scientist', 'HR'],
   [0.41061896397968545, 0.07778902787940564, 0.0, 0.0]],
  'Alex': [['Data Scientist', 'Data Engineer', 'SEO', 'HR'],
   [0.35533981037323636, 0.23559823858436493, 0.1180260997541829, 0.0]],
  'Melissa': [['HR', 'Content Writer', 'Data Scientist', 'ML Engineer'],
   [0.3051188401455247, 0.22159218133340636, 0.054504525110280415, 0.0]],
  'Kate': [['Senior Data Scientist',
    'ML Engineer',
    'Data Engineer',
    'Data Scientist'],
   [0.26055614634660734,
    0.2142955557589329,
    0.13912442613759962,
    0.11132743718042731]],
  'Sara': [['ML Engineer',
    'Senior Data Scientist',
    'Content Writer',
    'Data Scientist'],
   [0.43940522439009555, 0.20536409424587965, 0.04877455765945278, 0.0]],
  'John': [['HR', 'ML Engineer', 'Data Scientist', 'SEO'],
   [0.15915159600925785, 0.15038448206428018, 0.0, 0.0]],
  'Lisa': [['SEO', 'Data Scientist', 'HR', 'ML Engineer'],
   [0.22204389653588938, 0.0, 0.0, 0.0]],
  'Mohammad': [['MERN Stack Developer', 'Data Scientist', 'HR', 'ML Engineer'],
   [0.4259834700630331, 0.0, 0.0, 0.0]]},
 'job_fits': {'Data Scientist': [['Alex', 'Ebad', 'David', 'Kate'],
   [0.35533981037323636,
    0.3394664772663317,
    0.15722856214570313,
    0.11132743718042731]],
  'HR': [['David', 'Melissa', 'John', 'Ebad'],
   [0.44539723121318653, 0.3051188401455247, 0.15915159600925785, 0.0]],
  'ML Engineer': [['Sara', 'Kate', 'John', 'Andrew'],
   [0.43940522439009555,
    0.2142955557589329,
    0.15038448206428018,
    0.07778902787940564]],
  'SEO': [['Lisa', 'Alex', 'Ebad', 'Kate'],
   [0.22204389653588938,
    0.1180260997541829,
    0.07091927237638739,
    0.036977402538244546]],
  'Content Writer': [['Melissa', 'David', 'Sara', 'Ebad'],
   [0.22159218133340636, 0.0514383040706968, 0.04877455765945278, 0.0]],
  'Data Engineer': [['Alex', 'Ebad', 'Kate', 'David'],
   [0.23559823858436493,
    0.14156576967603743,
    0.13912442613759962,
    0.06556813089308454]],
  'Senior Data Scientist': [['Kate', 'Sara', 'Ebad', 'David'],
   [0.26055614634660734, 0.20536409424587965, 0.0, 0.0]],
  'Android Developer': [['Andrew', 'Ebad', 'David', 'Alex'],
   [0.41061896397968545, 0.0, 0.0, 0.0]],
  'MERN Stack Developer': [['Mohammad', 'Ebad', 'David', 'Andrew'],
   [0.4259834700630331, 0.0, 0.0, 0.0]],
  'Marketing Specialist': [['Ebad', 'David', 'Andrew', 'Alex'],
   [0.0, 0.0, 0.0, 0.0]]}}


# position_address = ['Henry Johnson Boulevard','Knox Street Historic District','Lark Street','Crosstown Arterial','Manning Boulevard']
# positions = data['jobs']
# candidate_names = ['    Liam', 'Olivia', 'Max', 'Noah', 'Charlotte']
# candidate_skills = ['Data, python', 'content writer, seo', 'data science, statistics', 'coding, software', 'content, marketing']

# candidate_address = ['Henry Johnson Boulevard', 'Lark Street','Henry Johnson Boulevard','Manning Boulevard','Crosstown Arterial']

# candidate_tenure = [1,2,3,1,3]

positions = data['jobs']
position_address = data['job_addresses']
candidate_names = data['candidate_names']
#candidate_skills = data['candidate_skills']
job_recommend = []
for key,value in data['candidates'].items():
    job_recommend.append(value[0][0])
#print(job_recommend)

cand_recommend = []
for key,value in data['job_fits'].items():
    cand_recommend.append(value[0][0])
print(cand_recommend)

candidate_skills = [w.replace(';', ',') for w in data['candidate_skills']]

skill_list = []
for skill in candidate_skills:
    skill_list.append(skill.split(",")[0])
#print(skill_list)
st.set_page_config(
    page_title="IOM",
    layout="wide"
)
download_df = pd.DataFrame(list(zip(candidate_names,candidate_skills,job_recommend)),columns=['Candidates','Skills','Top Job Recommendation'])
download_df2 = pd.DataFrame(list(zip(positions,position_address,cand_recommend)),columns=['Jobs','Address','Top Candidate Recommendation'])


st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 250px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 250px;
        margin-left: -250px;
    }
     
    """,
    unsafe_allow_html=True,
)
selected = st.sidebar.selectbox(
    "Menu",
    ("Jobs","Employees"),
   
)



# if selected == 'Jobs':
#     st.header("Job Recommendations")
    
#     tot_middle = []
  
#     df = pd.DataFrame(list(zip(candidate_names,skill_list,candidate_skills)),columns=['Candidates','Skills','complete_skills'])
#     #print(df_position_filter)
#     ind_skills = list(df['Skills'].str.split(",").values)
#     #print(ind_skills)
#     cand = st.sidebar.multiselect("Filter by Candidate Name", options=df['Candidates'].unique(),default=df['Candidates'])
#     skills = st.sidebar.multiselect("Filter by Candidate Skill", options=df['Skills'],default=df['Skills'])
#     #pos = st.sidebar.multiselect("Tenure", options=df['Tenure'].unique(),default=df['Tenure'].unique())
#     #print(skills)
#     df_filtered = df.query(
#         "Candidates == @cand & Skills == @skills"
#     )
#     #print(df_filtered.values)
    
    
#     col1, col2, col3 = st.columns([7,7,7])
#     #positions.insert(0,"")
#     with col1:
#         st.write("")
#         st.write("")
#         @st.cache
#         def convert_df(df):
#                 # IMPORTANT: Cache the conversion to prevent computation on every rerun
#             return df.to_csv().encode('utf-8')

#         csv = convert_df(download_df)

#         st.download_button(
#             label="Download Recommendations",
#             data=csv,
#             file_name='job_recommendations.csv',
#             mime='text/csv',
#         )
#         st.write("")
#         st.write("")
#         count = 0
#         for i in df_filtered.values:
#             #print(i)
#             if count != 0:
#                 st.write("")
#                 st.write("")
                
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.container()
#             count+=1
#             st.image('male2.png')
            
#             st.write("Name:",i[0])
#             st.write("Skills:",i[2])
#                 #st.write("Address:",df_filtered['Candidates'].values[i])
#             #st.write("Tenure:",i[0])
   
#     with col2:
        
       
#         # check df filtered, if name not there then don't show that person's slider too
#         #print(df_filtered['Candidates'].values)
#         count = 100
#         tot_list = []
#         tot_list2 = []
       
       
#         st.write("")
#         st.write("")
#         st.write("")
#         st.write("")
#         st.write("")
#         st.write("")
      
#         for name in candidate_names:
#             if name in df_filtered['Candidates'].values:
#                 no_jobs_1 = st.slider('Number of Jobs', 1, len(data['candidates'][name][0]), len(data['candidates'][name][0]) - 2, key =count)
#                 count+=1
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
               
            

        

                
#                 split_list = []
#                 split_list2 = []
#                 split_middle = []
#                 for i in range(no_jobs_1):
                    
#                     split_list.append(data['candidates'][name][0][i])
#                     split_middle.append(data['candidates'][name][0][i])
#                     split_list2.append(data['candidates'][name][1][i])
#                     # counter+=1
#                     # if counter == 2:
#                     #     counter = 0
#                 tot_middle.append(split_middle)
#                 if len(split_list) < 4:
#                     length = len(split_list)
#                     iterate = 4 - length
#                     for i in range(iterate):
#                         split_list.append("empty")
#                         split_list2.append("empty")
#                 tot_list.append(split_list)
#                 tot_list2.append(split_list2)
#         print(tot_middle)
#         #st.write("No. of jobs: ", no_jobs_1)
#     with col3:
#         # st.write("")
#         # st.write("")
        
#         threshold = st.selectbox("Choose Threshold", ('All','>50%', '>3%'))
     
#         if threshold == 'All':
#             threshold = 0
#         elif threshold == '>50%':
#             threshold = 0.5
#         elif threshold == '>3%':
#             threshold = 0.03
#         st.write("")
#         st.write("")
#         st.write("")
#         st.write("")
     
#         for i in range(len(tot_list)):
#             for j in range(len(tot_list[i])):
#             #st.write(positions[i])
                
#                 if tot_list[i][j] != 'empty':
#                     #print(tot_list[i][j])
#                     if tot_list2[i][j] >= threshold:


                    
                
                  
#             #st.markdown('<h5>{} {}</h5>'.format("Job:",positions[i]),unsafe_allow_html=True)
         
#             #st.markdown('<h6>Job Description</h6><p style="margin-left: 1.5em;">{}</p>'.format(positions[i]),unsafe_allow_html=True)
#                         st.markdown('<p style="margin-left: 3em;padding: 3px 5px 2px 20px;border-width: 4px; border-color: red; border-style:solid;"><u>{}</u><br></br></p>'.format(tot_list[i][j]),unsafe_allow_html=True)
#                     else:
#                         st.write("")
#                         st.write("")
#                         st.write("")
#                         st.write("")
#                         st.write("")
                     

#                 else:
#                     st.write("")
#                     st.write("")
#                     st.write("")
#                     # st.write("")
#                     st.write("")
#                     st.write("")
                 
               
#                     # st.write("")
#                     # st.write("")
#                     # st.write("")
                        
                   

           
           
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             #st.write("")
#             st.write("")
          
#             # st.write("")
#             # st.write("")
            
            
#             #st.markdown('<h5></h5><p style="margin-left: 2.5em;padding: 0em 3em 0em 0em;border-width: 3px; border-color: red; border-style:dashed;"><u>{}</u><br></br>{}</p>'.format(positions[i],position_address[i]),unsafe_allow_html=True)
  
        
#     # with col4:
      
#     #     count = 0
#     #     for i in tot_list:
#     #         for j in i:
#     #             st.write("")
#     #             st.write("")
#     #             if j != 'empty':
#     #                 val1 = st.checkbox("", value=True, key = count+1)
#     #                 print(val1)
                    
                  
#     #                 st.write("")
#     #                 # st.write("")
#     #                 # st.write("")
#     #                 # st.write("")
#     #             else:
#     #                 #st.write("")
#     #                 st.write("")
#     #                 st.write("")
#     #                 st.write("")
#     #                 st.write("")
#     #                 st.write("")
#     #                 st.write("")
#     #                 st.write("")
          
#                     # if count > 3:
#                     #     st.write("")
#                     #     st.write("")
                        
#                     # st.write("")
#                     # st.write("")
#                     # st.write("")

                
#             #     count+=1
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             #st.write("")
            
#     #     st.write("")
#     #     st.write("")
#     #     for i in split_list[1]:
#     #         #st.write(positions[i])
           
#     #         #st.markdown('<h5>{} {}</h5>'.format("Job:",positions[i]),unsafe_allow_html=True)
         
#     #         #st.markdown('<h6>Job Description</h6><p style="margin-left: 1.5em;">{}</p>'.format(positions[i]),unsafe_allow_html=True)
#     #         st.markdown('<p style="margin-left: 2.5em;padding: 3px 5px 2px 20px;border-width: 4px; border-color: red; border-style:solid;"><u>{}</u><br></br></p>'.format(i),unsafe_allow_html=True)

# if selected == 'Employees':
#     st.header("Candidate Recommendations")
    
#     tot_middle = []
  
#     df = pd.DataFrame(list(zip(positions,position_address)),columns=['Jobs','Address'])
#     #print(df_position_filter)
#     #ind_skills = list(df['Skills'].str.split(",").values)
#     #print(ind_skills)
#     job = st.sidebar.multiselect("Filter by Job Name", options=df['Jobs'].unique(),default=df['Jobs'])
#     address = st.sidebar.multiselect("Filter by Job Address", options=df['Address'].unique(),default=df['Address'])
#     #pos = st.sidebar.multiselect("Tenure", options=df['Tenure'].unique(),default=df['Tenure'].unique())
#     #print(skills)
#     df_filtered2 = df.query(
#         "Jobs == @job & Address == @address"
#     )
#     #print(df_filtered.values)
    
    
#     col1, col2, col3 = st.columns([7,7,7])
#     #positions.insert(0,"")
#     with col1:
#         st.write("")
#         st.write("")
#         @st.cache
#         def convert_df(df):
#                 # IMPORTANT: Cache the conversion to prevent computation on every rerun
#             return df.to_csv().encode('utf-8')

#         csv = convert_df(download_df2)

#         st.download_button(
#             label="Download Recommendations",
#             data=csv,
#             file_name='employee_recommendations.csv',
#             mime='text/csv',
#         )
#         st.write("")
#         st.write("")
#         st.write("")
#         #st.write("")
#         #st.write("")
#         # st.write("")
#         count = 0
#         for i in df_filtered2.values:
#             #print(i)
#             if count > 0:
#                 # st.write("")
#                 # st.write("")
                
#                 # st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 #st.write("")
#                 # st.write("")
#                 # st.write("")
#                 # st.write("")
#             if count > 1:
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#             # if count > 6:
#             #     st.write("")
               
           

#             count+=1
#             #st.image('male2.png')
#             st.markdown('<h2>{}</h2>'.format(i[0]),unsafe_allow_html=True)

#             # st.write("Job:",i[0])
#             st.write("Address:",i[1])
#                 #st.write("Address:",df_filtered['Candidates'].values[i])
#             #st.write("Tenure:",i[0])
   
#     with col2:
        
       
#         # check df filtered, if name not there then don't show that person's slider too
#         #print(df_filtered['Candidates'].values)
#         count = 100
#         tot_list = []
#         tot_list2 = []
       
       
#         st.write("")
#         st.write("")
#         st.write("")
#         st.write("")
#         st.write("")
#         st.write("")
#         st.write("")
#         print(tot_middle)
#         for name in positions:
#             if name in df_filtered2['Jobs'].values:
#                 no_jobs_1 = st.slider('Number of Employees', 1, len(data['job_fits'][name][0]), len(data['job_fits'][name][0]) - 2, key =count)
#                 count+=1
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 st.write("")
#                 if count > 106:
#                     st.write("")
#                     st.write("")
#                     st.write("")
                
            

        

                
#                 split_list = []
#                 split_list2 = []
#                 split_middle = []
#                 for i in range(no_jobs_1):
                    
#                     split_list.append(data['job_fits'][name][0][i])
#                     split_middle.append(data['job_fits'][name][0][i])
#                     split_list2.append(data['job_fits'][name][1][i])
#                     # counter+=1
#                     # if counter == 2:
#                     #     counter = 0
#                 tot_middle.append(split_middle)
#                 if len(split_list) < 4:
#                     length = len(split_list)
#                     iterate = 4 - length
#                     for i in range(iterate):
#                         split_list.append("empty")
#                         split_list2.append("empty")
#                 tot_list.append(split_list)
#                 tot_list2.append(split_list2)
#         print(tot_middle)
#         #st.write("No. of jobs: ", no_jobs_1)
#     with col3:
#         # st.write("")
#         # st.write("")
        
#         threshold = st.selectbox("Choose Threshold", ('All','>30%', '>3%'))
     
#         if threshold == 'All':
#             threshold = 0
#         elif threshold == '>30%':
#             threshold = 0.3
#         elif threshold == '>3%':
#             threshold = 0.03
#         st.write("")
#         st.write("")
#         st.write("")
#         st.write("")
#         # st.write("")
#         count = 0
#         for i in range(len(tot_list)):
#             for j in range(len(tot_list[i])):
#             #st.write(positions[i])
                
#                 if tot_list[i][j] != 'empty':
#                     #print(tot_list[i][j])
#                     if tot_list2[i][j] >= threshold:



                    
                
                  
#             #st.markdown('<h5>{} {}</h5>'.format("Job:",positions[i]),unsafe_allow_html=True)
         
#             #st.markdown('<h6>Job Description</h6><p style="margin-left: 1.5em;">{}</p>'.format(positions[i]),unsafe_allow_html=True)
#                         st.markdown('<p style="margin-left: 3em;padding: 3px 5px 2px 20px;border-width: 4px; border-color: red; border-style:solid;"><u>{}</u><br></br></p>'.format(tot_list[i][j]),unsafe_allow_html=True)
#                     else:
#                         st.write("")
#                         st.write("")
#                         st.write("")
#                         st.write("")
#                         st.write("")
#                         st.write("")
#                         st.write("")
#                         if count > 9:
#                             st.write("")
#                             st.write("")

                     

#                 else:
#                     count +=1
#                     st.write("")
#                     st.write("")
#                     st.write("")
#                     # st.write("")
#                     st.write("")
#                     #st.write("")
#                     if count > 9:
#                         st.write("")
#                         #st.write("")
#                         # st.write("")

                 
               
#                     # st.write("")
#                     # st.write("")
#                     # st.write("")
                        
                   

           
           
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             st.write("")
#             #st.write("")
#             #st.write("")
#             if count >1:
#                 st.write("")
#                 st.write("")
#                 st.write("")
                
         

          
#             # st.write("")
#             # st.write("")
            
            
#             #st.markdown('<h5></h5><p style="margin-left: 2.5em;padding: 0em 3em 0em 0em;border-width: 3px; border-color: red; border-style:dashed;"><u>{}</u><br></br>{}</p>'.format(positions[i],position_address[i]),unsafe_allow_html=True)
  
        
#     # with col4:
      
#     #     count = 0
#     #     for i in tot_list:
#     #         for j in i:
#     #             st.write("")
#     #             st.write("")
#     #             if j != 'empty':
#     #                 val1 = st.checkbox("", value=True, key = count+1)
#     #                 print(val1)
                    
                  
#     #                 st.write("")
#     #                 # st.write("")
#     #                 # st.write("")
#     #                 # st.write("")
#     #             else:
#     #                 #st.write("")
#     #                 st.write("")
#     #                 st.write("")
#     #                 st.write("")
#     #                 st.write("")
#     #                 st.write("")
#     #                 st.write("")
#     #                 st.write("")
          
#                     # if count > 3:
#                     #     st.write("")
#                     #     st.write("")
                        
#                     # st.write("")
#                     # st.write("")
#                     # st.write("")

                
#             #     count+=1
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             # st.write("")
#             #st.write("")
            
#     #     st.write("")
#     #     st.write("")
#     #     for i in split_list[1]:
#     #         #st.write(positions[i])
           
#     #         #st.markdown('<h5>{} {}</h5>'.format("Job:",positions[i]),unsafe_allow_html=True)
         
#     #         #st.markdown('<h6>Job Description</h6><p style="margin-left: 1.5em;">{}</p>'.format(positions[i]),unsafe_allow_html=True)
#     #         st.markdown('<p style="margin-left: 2.5em;padding: 3px 5px 2px 20px;border-width: 4px; border-color: red; border-style:solid;"><u>{}</u><br></br></p>'.format(i),unsafe_allow_html=True)
