clc
clear all
close all
path0 = './img/v6/';
namelist = dir('./img/v6/*.jpg');
len = length(namelist);
scs = 54; % 描述
interval = len/scs;
imgs = cell(scs,1);
track = cell(scs,1);
tracks = zeros(scs,2);
count = 0;
level = 0.5;
th_for_edge = 0.2;
mask = ones
roi = [200:500,400:1000];
%roi = [200:300,400:800]; % v3的roi要改成这一行
for i = 1:interval:len
    i = floor(i);
    count = count + 1;
    file_name{i}=namelist(i).name;
    imgs{count,1}= imread([path0,file_name{i}]);
    [h,w,c] = size(imread([path0,file_name{i}]));
end

for j = 1:length(imgs)
    img = imgs{j};
    img = img(200:500,400:800,:); % 提取roi区域
    img_gray = rgb2gray(img);
    sigma=6;%标准差大小
    window=double(uint8(3*sigma)*2+1);%窗口大小一半为3*sigma

    H=fspecial('gaussian', window, sigma);%fspecial('gaussian', hsize, sigma)产生滤波模板
    %为了不出现黑边，使用参数'replicate'（输入图像的外部边界通过复制内部边界的值来扩展）
    img_gauss=imfilter(img_gray,H,'replicate');
    bw=im2bw(img_gauss,level); %找到所有连通区域
    % 找到小球所在位置   
    bw = ~bw;
    sum_row  = sum(bw,2);
    [row,temp]=find(sum_row~=0);
    row_final = max(row);
    %col_final = col_final(1);
    col_full = bw(row_final ,:);
    col_final = find(col_full==max(col_full));
    col_final = sum(col_final)/length(col_final);
    track{j} = [row_final;col_final];
    tracks(j,1) = row_final;
    tracks(j,2) = col_final;
    %imshow(bw)  % 这一行可以注释掉看过程
    hold on 
    [h,w] = size(img_gray);
    blank = 255*ones(h,w);
    imshow(blank)
    %hold on 
    
    %bw = edge(img_gauss,'Canny',th_for_edge);
    %bw=im2bw(img_gray,level);
    %temp = 1;
end
plot(tracks(:,2),tracks(:,1),'-');
save track_v6 tracks
