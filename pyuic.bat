SET ENV=C:\Users\Seeking\Anaconda3\envs\pyqt5
SET pyuic=%ENV%\Scripts\pyuic5

SET ROOT=D:\llf\code\tiny-backup/view
SET INPUT_DIR=%ROOT%\ui
SET OUTPUT_DIR=%ROOT%\py

SET FILE_NAME=main

SET INPUT=%INPUT_DIR%\%FILE_NAME%.ui
SET OUTPUT=%OUTPUT_DIR%\%FILE_NAME%.py

%pyuic% -o %OUTPUT% %INPUT%
