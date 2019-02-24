#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'workspace\.ipynb_checkpoints'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Writing my first Python code

#%%
# Hello World in python
# print is a function
print ("Hello World!")


#%%
x = 5
y = 7

x = 100



#%%
print(x+y)
print(x+y)


#%%



