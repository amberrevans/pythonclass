#Amber Evans
#10-8-2020
#program 6-11
#This program saves a sequence of video running times
#to the video_times.txt file.

def main():
    #get the number of videos in the project
    num_videos=int(input('How many videos are in the project?'))

    #open the file to hold the running times
    video_file=open('video_times.txt','w')

    #get each videos  running time and write
    #it to the file
    print('Enter the running times for each video.')
    for count in range (1, num_videos+1):
        run_time=float(input(f'Video #{count}: '))
        video_file.write(f'{run_time}\n')

    #close the file
    video_file.close()
    print('The times have been saved to video_times.txt.')

#Call the main function
if __name__=='__main__':
    main()
    
