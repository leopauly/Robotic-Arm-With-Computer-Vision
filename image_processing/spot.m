%Calculates the number of symmetric dark spots in the image which has a size of 4 pixels or less.

clc
clear
img=imread('al3.jpg');
img;
n=size(img);
img=double(img);
spot=0;
t=200
for i=1:(n(1)-4)
   for j=1:(n(2)-4)
        w=1;
    for x=1:4
    for y=1:4
        k(w)=(img(i+x,j+y,1)+img(i+x,j+y,2)+img(i+x,j+y,3));
        w=w+1;
    end
    end
    
    
    if((k(6)<t && k(7)<t && k(10)<t && k(11)<t) && k(1)>t && k(2)>t && k(3)>t && k(4)>t &&  k(5)>t && k(8)>t && k(9)>t && k(12)>t &&  k(13)>t && k(14)>t && k(15)>t && k(16)>t )
        spot=spot+1;
    end
        
  end
end
for i=1:(n(1)-4)
   for j=1:(n(2)-4)
        w=1;
    for x=1:3
    for y=1:3
        k(w)=(img(i+x,j+y,1)+img(i+x,j+y,2)+img(i+x,j+y,3));
        w=w+1;
    end
    end
    
    
    if((k(5)<t)&& k(1)>t && k(2)>t && k(3)>t && k(4)>t &&  k(6)>t && k(8)>t && k(9)>t && k(7)>t)
      spot=spot+1;
    end
        
  end
end
for i=1:(n(1)-4)
   for j=1:(n(2)-4)
        w=1;
    for x=1:4
    for y=1:3
        k(w)=(img(i+x,j+y,1)+img(i+x,j+y,2)+img(i+x,j+y,3));
        w=w+1;
    end
    end
    
    
    if((k(5)<t)&& k(8)<t && k(1)>t && k(2)>t && k(3)>t && k(4)>t &&  k(6)>t && k(10)>t && k(9)>t && k(7)>t && k(11)>t && k(12)>t)
      spot=spot+1;
    end
        
  end
end
img=uint8(img);
spot
size(img)
figure,imshow(img)
str = num2str(spot);
    msgbox(str);
            
            
            
