
from keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model('model.h5')
model.make_predict_function()

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(100,100))
	i = image.img_to_array(i)/255.0
	i = i.reshape(1, 100,100,3)
	p = model.predict(i)
	if(p[0][0] > p[0][1]):
		return "Mask on"
	else:
		return "No Mask detected"
msk=0
nmsk=0
for i in range(1,30):
    img='DataSets/DataSets/Maskless/1 ('+str(i)+').jpg'
    p=predict_label(img)
    print(p)
    if p=="Mask on":
        msk+=1
    else:
        nmsk+=1
print("hai")
print(msk,nmsk)