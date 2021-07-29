import psutil
import pandas

def getProcesses():
    '''
    Get a list of all running processes
    Output Process ID, Process Name, Memory Util
    '''
    listOfProcesses = []
    for process in psutil.process_iter():
        try:
            # Fetch processes as dict
            pinfo = process.as_dict(attrs=['pid', 'name'])
            pinfo['Process ID'] = pinfo.pop('pid')
            pinfo['Process Name'] = pinfo.pop('name')
            pinfo['Memory Utilization(bytes)'] = process.memory_info().vms
            listOfProcesses.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listOfProcesses

def generateCSV():
    '''
    Generate the CSV of the running processes
    Output the file in the current directory
    '''
    results = getProcesses()
    df = pandas.DataFrame(results)
    df.to_csv('processes.csv', index=False)