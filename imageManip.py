# CMPT 120 Yet Another Image Processer
# Author(s): Ronney Lok, Kevin Hau
# Date: Dec 7th, 2020
# Description: A module file to organize functions so that the main code in main.py
# can easily call it from there.

import cmpt120imageProj
import numpy


#def the function to invert(pixels)
def invert(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])
  #goes through each pixel
  for column in range(length):
    for row in range(height):
      #to zero in on one pixel
      p = pixels[column][row]
      #inverts the colour here
      new_r = 255 - p[0]
      new_g = 255 - p[1]
      new_b = 255 - p[2]
      #set as manipulated image
      newImg[column][row] = [new_r,new_g,new_b]

  return newImg

#def the function to flip horizontally
def flipHorizontal(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])
  #get last column
  l_column = (length-1)
    #go through each pixel
  for column in range(length):
    for row in range(height):
      #change last column to first
      n_column = l_column - column
      newImg[column][row] = pixels[n_column][row]

  

  return newImg

#def the function to flip vertically
def flipVertical(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])
  l_row = (height-1)
  for column in range(length):
    for row in range(height):

      n_row = l_row - row
      newImg[column][row] = pixels[column][n_row]
  
  
  return newImg

#def the function remove red
def remove_red(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])
  #goes through each pixel
  for column in range(length):
    for row in range(height):

      p = pixels[column][row]
      new_r = p[0]=0
      
      newImg[column][row] = [new_r,p[1],p[2]]

  return newImg

#def the function remove green
def remove_green(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])
  for column in range(length):
    for row in range(height):
      #turns green to 0
      p = pixels[column][row]
      new_g = p[1]=0
      
      newImg[column][row] = [p[0],new_g,p[2]]

  return newImg

#def the function remove blue
def remove_blue(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])
  for column in range(length):
    for row in range(height):
      #turns blue to 0
      p = pixels[column][row]
      new_b = p[2]=0
      
      newImg[column][row] = [p[0],p[1],new_b]

  return newImg

#def the function converts to grayscale
def gray_scale(pixels):
  length = len(pixels)
  height = len(pixels[0])
  for column in range(length):
    for row in range(height):
      #gets the average and turns rgb to avg (greyscale)
      p = pixels[column][row]
      avg=(p[0]+p[1]+p[2])/3
      new_r = p[0]=avg
      new_g = p[1]=avg
      new_b = p[2]=avg

      pixels[column][row] = [new_r,new_g,new_b]

  return pixels

#def the function sepia filter
def sepia_filter(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])
  #sets maxrgb 255
  maxrgb=255
  for column in range(length):
    for row in range(height):
      p = pixels[column][row]
      #does calculation for sepia filter
      calc_r=(p[0]*0.393)+(p[1]*0.769)+(p[2]*0.189)
      calc_g=(p[0]*0.349)+(p[1]*0.686)+(p[2]*0.168)
      calc_b=(p[0]*0.272)+(p[1]*0.534)+(p[2]*0.131)
      maxrgb=255
      #if value of each colour is bigger than maxrgb, than the colour will become maxrgb
      if calc_r>maxrgb:
        calc_r=maxrgb
        
      if calc_g>maxrgb:
        calc_g=maxrgb
        
      if calc_b>maxrgb:
        calc_b = maxrgb
     
      new_r = p[0]=int(calc_r)
      new_g = p[1]=int(calc_g)
      new_b = p[2]=int(calc_b)

      newImg[column][row] = [new_r,new_g,new_b]

  return newImg

#def the function decrease brightness
def decrease_brightness(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])
  for column in range(length):
    for row in range(height):
      #each colour minus 10
      p = pixels[column][row]
      new_r = p[0]-10
      new_g = p[1]-10
      new_b = p[2]-10
      #set 0 as the lowest it can go
      if new_r <0:
          new_r = 0
      if new_g <0:
          new_g = 0
      if new_b <0:
          new_b=0
        
      newImg[column][row] = [new_r,new_g,new_b]

  return newImg

#def the function increase brightness
def increase_brightness(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])
  for column in range(length):
    for row in range(height):
      #each colour add 10
      p = pixels[column][row]
      new_r = p[0]+10
      new_g = p[1]+10
      new_b = p[2]+10
      #set 255 as the highest it can go
      if new_r >255:
          new_r = 255
      if new_g >255:
          new_g = 255
      if new_b >255:
          new_b=255
      
      newImg[column][row] = [new_r,new_g,new_b]

  return newImg

#def the function rotate left
def rotate_left(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])
  #makes the height and length swap
  newImg = cmpt120imageProj.createBlackImage(height,length)
  for column in range(length):
    for row in range(height):
      y = length-1-column
      newImg[row][y] = pixels[column][row]
  
  return newImg

#def the function rotate right
def rotate_right(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])
  # makes the height and length swap
  newImg = cmpt120imageProj.createBlackImage(height,length)
  for column in range(length):
    for row in range(height):
      # gets the last value 
      x = height-1-row
      # assigning the new image with x now as the x value and the column as the y value in the image
      newImg[x][column] = pixels[column][row]
  
  return newImg

#def the function pixelate 
def pixelate(pixels, newImg):
  length = len(pixels)
  height = len(pixels[0])

  num_pixels = 16
  
  #sees if image is dividable by 4, if not it cuts out the excess
  if length % 4 == 1:
    length -= 1
  if length % 4 == 2:
    length -= 2
  if length % 4 == 3:
    length -=3 
  if height % 4 == 1:
    height -= 1
  if height % 4 == 2:
    height -= 2
  if height % 4 == 3:
    height -= 3
  # breaks pixels into 4 by 4
  for column in range(0,length,4):
    for row in range(0,height,4):
      #sets values
      p_counter=[0,0,0]
      r_counter=0
      g_counter=0
      b_counter=0
      #goes through pixel
      for l in range(4):
        for r in range(4):
          p = pixels[column][row]
          p_counter += str(l)
          #sets new colours
          lr_counter=p_counter[0]
          lg_counter=p_counter[1]
          lb_counter=p_counter[2]
          


          #finds average by dividing by 16
          new_r = (lr_counter)/ num_pixels
          new_g = (lg_counter) / num_pixels
          new_b = (lb_counter) / num_pixels
          pixels[column][row] = [new_r,new_g,new_b]

  
  

  return pixels
      
#def the function binarize
def binarize(pixels, newImg):
  newImg = gray_scale(pixels) 
  length = len(newImg)
  height = len(newImg[0])
  all_pixels = length * height
  threshold_accumulator = 0

  # calculate the initial threshold 
  for column in range(length):
    for row in range(height):
      threshold_accumulator += newImg[column][row][0]

  init_threshold = threshold_accumulator / all_pixels

  # keep looping unitl the the difference in thresholds are less than or eqaul to 10
  cond = True
  while cond:
    # initialize variables
    background = []
    foreground = []
    background_accumulator = 0
    foreground_accumulator = 0

    for column in range(length):
      for row in range(height):
        p = newImg[column][row]

        # if the pixels have value less than or equal to the threshold, the pixels belong in the background image
        # if the pixels have value grater than the threshold, the pixels pbelong in the foreground image
        if p[0] <= init_threshold:
          background += [p]
        elif p[0] > init_threshold:
          foreground += [p]

    # finding the average of the background and foreground
    # the average 
    for rgb in background:
        background_accumulator += rgb[0]
    for rgb in foreground:
        foreground_accumulator += rgb[0]
    
    average_background = background_accumulator / all_pixels

    average_foreground = foreground_accumulator / all_pixels

    threshold = (average_background + average_foreground) // 2

    # if the difference between the initial and new threshold is less than or equal to 10, then the new threshold is the desired threshold. exit the while loop
    # if the difference in thresholds is grater than 10, repeat while loop with the initial threshold being the new threshold
    if init_threshold - threshold <= 10:
      cond = False
    else:
      init_threshold = threshold      

  # if the pixel is less than or equal to the threshold value set it to black
  # if the pixel is grater than the threshold value set it to white
  for column in range(length):
    for row in range(height):
      gray_scale_p = newImg[column][row]

      if gray_scale_p[0] <= threshold:
        newImg[column][row] = [0,0,0]
      elif gray_scale_p[0] > threshold:
        newImg[column][row] = [255,255,255]
  
  return newImg





