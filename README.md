# NoteHub
NotHub is an optical character recognition based desktop app that converts lecture notes (or any other notes) from an image to a text format such as a pdf. It is meant to aid students with physical disabilities take notes by converting images to searchable and editable text.

- OpenCV with Python is used for initial image processing, either by selecting files from the computer or taking live photos through webcam
- Microsoft Azure's cognitive services are then used to convert the image into ASCII characters within text file format
- The processed text is then converted to other file formats such as a pdf and the file is stored on the computer locally
- Images can also be uploaded to web based platforms. In the case of the hackathon, Imgur was used.

