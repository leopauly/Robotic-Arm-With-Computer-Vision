% The code calculates the number of pixels corresponding to the 
% defective portions on the surface of the mango from the image.


clc
clear
img=imread('area1.jpg');
img;
imshow(img);
n=size(img);
img=double(img);

spot=0;

for i=1:n(1)
    for j=1:n(2)
        if((img(i,j,1)+img(i,j,2)+img(i,j,3))>250)
            
            img(i,j,1)=0;
            img(i,j,2)=0;
            img(i,j,3)=0;
        else
            spot=spot+1;
            img(i,j,1)=255;
            img(i,j,2)=255;
            img(i,j,3)=255;
        end
    end
end

img=uint8(img);
spot
figure,imshow(img)

size(img)
str = num2str(spot);
msgbox(str,'dark pixels');
