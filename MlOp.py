#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import Sequential
from keras_preprocessing.image import ImageDataGenerator


# In[2]:


model = Sequential()


# In[3]:


model.add(Convolution2D(filters=8, 
                        kernel_size=(3,3), 
                        activation='relu',
                   input_shape=(64, 64, 3)
                       ))
model.add(MaxPooling2D(pool_size=(2, 2)))


# In[4]:


with open("/data/data/COUNT.txt","r") as myfile:
   c=(myfile.readlines())
   count=int(c[0])


# In[5]:


def l(a,c,size):
    model.add(Convolution2D(filters=a, 
                        kernel_size=(size,size), 
                        activation='relu',
                   
                       ))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dense(units=128, activation='relu'))
    
    global count
    count=c+1


# In[ ]:


l(16,count,3)




# In[ ]:


model.add(Flatten())


# In[ ]:


model.add(Dense(units=1, activation='sigmoid'))


# In[ ]:


model.summary()


# In[ ]:


model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# In[ ]:


train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(
        '/data/data/train/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        '/data/data/validation/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
model.fit(
        training_set,
        steps_per_epoch=100,
        epochs=15,validation_data=test_set,validation_steps=10)


# In[ ]:


scores = model.evaluate(test_set,  verbose=1)
print(scores[1]*100,file=open("/data/data/acc.txt","w"),end="")
scores[1]


# In[ ]:


print(count,file=open("/data/data/COUNT.txt","w"),end="")
count


# In[ ]:




