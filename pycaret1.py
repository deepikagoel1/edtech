from xml.etree.ElementPath import prepare_star
from pycaret.nlp import load_model

def recommend(course):
    
    courses_list = load_model('C:/Users/Deepika/Downloads/benchprep/course_list')
    similarity = load_model('C:/Users/Deepika/Downloads/benchprep/similarity')
    courses = load_model('C:/Users/Deepika/Downloads/benchprep/courses')

    index = courses_list[courses_list['course_name'] == course].index[0]
    print("Course", index)
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    print("Distances, distances")
    recommended_course_names = []
    for i in distances[1:7]:
        course_name = courses_list.iloc[i[0]].course_name
        recommended_course_names.append(course_name)

    return recommended_course_names

def get_output_schema():
     return pd.DataFrame({
     'Recommend Course' : prep_string(),
     'course_id' : prep_string(),
     'Course_Name' : prep_string(),
     'Tenant' : prep_string(),
     'Difficulty_Level' : prep_string(),
     'Course Rating' : prep_string(),
     'Course_URL' : prep_string(),
     'Course_Description' : prep_string(),
     'Skills' : prep_string(),
     'members' : prep_int()
     })
