# import time
# from moviepy.editor import concatenate_audioclips, AudioFileClip
# import random
# import os

# class conCatFile:
#     def __init__(self, absPathFolderContainSong):
#         self.inputListMP3 = []  # Initialize as empty list
#         self.resultMP3 = "result.mp3"
#         self.path = absPathFolderContainSong
#         self.filenames = os.listdir(self.path)
#         self.downloadPath = "downloads"
        
#         if not os.path.exists(self.downloadPath):
#             os.makedir(self.downloadPath)
            
            
#     def setPath(self, absPathFolderContainSong):
#         self.path = absPathFolderContainSong

#     def getPath(self):
#         return self.path

#     def setListInputMP3(self, inputListMP3: list):
#         self.inputListMP3 = inputListMP3

#     def getListInputMP3(self):
#         return self.inputListMP3

#     def getFileNames(self):
#         return self.filenames

#     def getResultFile(self):
#         return os.path.join(self.downloadPath, self.resultMP3)

#     def conCatFileMP3(self):
#         randomIndexList = []
#         for filename in self.getFileNames():
#             self.getListInputMP3().append(os.path.join(self.getPath(), filename))

#         randomListInputFile = []
#         while len(self.getListInputMP3()) > 0:
#             index = random.randint(0, len(self.getListInputMP3()) - 1)
#             file_path = self.getListInputMP3()[index]

#             try:
#                 audio_clip = AudioFileClip(file_path)
#                 randomListInputFile.append(audio_clip)
#                 randomIndexList.append(file_path)  # Append the file name to the result list
#             except Exception as e:
#                 print(f"Error loading {file_path}: {e}")

#             self.getListInputMP3().pop(index)

#         if randomListInputFile:
#             start = time.time()
#             final = concatenate_audioclips(randomListInputFile)
#             result_file_path = self.getResultFile()
#             final.write_audiofile(result_file_path)
#             end = time.time()
#             timeTaken = end-start
#             print("concatFileMP3 finished!")
#         else:
#             print("No valid MP3 files to concatenate.")

#         return timeTaken,randomIndexList






import time
from moviepy.editor import concatenate_audioclips, AudioFileClip
import random
import os

class conCatFile:
    def __init__(self, absPathFolderContainSong):
        self.inputListMP3 = []  # Initialize as empty list
        self.resultMP3 = "result.mp3"
        self.path = absPathFolderContainSong
        self.filenames = os.listdir(self.path)
        self.downloadPath = "downloads"
        
        if not os.path.exists(self.downloadPath):
            os.makedirs(self.downloadPath)  # Changed from os.makedir to os.makedirs
            
    def setPath(self, absPathFolderContainSong):
        self.path = absPathFolderContainSong

    def getPath(self):
        return self.path

    def setListInputMP3(self, inputListMP3: list):
        self.inputListMP3 = inputListMP3

    def getListInputMP3(self):
        return self.inputListMP3

    def getFileNames(self):
        return self.filenames

    def getResultFile(self):
        return os.path.join(self.downloadPath, self.resultMP3)

    def conCatFileMP3(self):
        randomIndexList = []
        for filename in self.getFileNames():
            self.getListInputMP3().append(os.path.join(self.getPath(), filename))

        randomListInputFile = []
        while len(self.getListInputMP3()) > 0:
            index = random.randint(0, len(self.getListInputMP3()) - 1)
            file_path = self.getListInputMP3()[index]

            try:
                audio_clip = AudioFileClip(file_path)
                randomListInputFile.append(audio_clip)
                randomIndexList.append(file_path)  # Append the file name to the result list
            except Exception as e:
                print(f"Error loading {file_path}: {e}")

            self.getListInputMP3().pop(index)

        timeTaken = None
        if randomListInputFile:
            start = time.time()
            final = concatenate_audioclips(randomListInputFile)
            result_file_path = self.getResultFile()
            final.write_audiofile(result_file_path)
            end = time.time()
            timeTaken = end - start
            print("concatFileMP3 finished!")
        else:
            print("No valid MP3 files to concatenate.")

        return timeTaken, randomIndexList
