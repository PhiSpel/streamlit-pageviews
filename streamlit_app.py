import streamlit as st


#@st.cache()
#def page_view_counter(page_views):
#    page_view_counter+=1
#    return page_view_counter
    
@st.cache(allow_output_mutation=True)
def global_page_views():
    gpv = 0 # this will only be run once because after the first execution the cache will be referenced
    return gpv
    
@st.cache(allow_output_mutation=True)
def session_execution_counter():
    sec = 0 # this will only be run once because after the first execution the cache will be referenced
    return sec

@st.cache(allow_output_mutation=True)
def session_execution_counter_history():
    sec_history = [] # this will only be run once because after the first execution the cache will be referenced
    return sec_history

st.title('Trying out page view counts with caching.')
    
if not 'session_executions' in st.session_state:
    # this will only be run once per session
    gpv = global_page_views() # initialize the global page views variable (activates the cache)
    gpv += 1 # this should raise the global_page_views() output by one globally
    #page_views = page_view_counter(page_views)
    sec = session_execution_counter() # get the sec from previous session
    sec_history = session_execution_counter_history() # get sec history from global cache
    sec_history.append(sec) # append sec from previous session to global counter
    sec = 1 # this will globally set the sec to 1
    st.session_state.session_executions = 'something'
else:
    sec = session_execution_counter()
    sec += 1 # returns one more than it previously was and caches it
    
st.write('current page views: ' + str(page_views))
st.write('current session executions: ' + str(sec))

st.button('rerun')
