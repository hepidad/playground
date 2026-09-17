function createDriveFolders() {
  // Replace with the ID of your target Google 
Drive folder
  const PARENT_FOLDER_ID = 
' '; 
  
  const folderNames = [
    '1. FOLDER1',
    '2. FOLDER2',
    '3. FOLDER3'
  ];

  const parentFolder = 
DriveApp.getFolderById(PARENT_FOLDER_ID);
  
  folderNames.forEach(name => {
    parentFolder.createFolder(name);
    Logger.log('Created: ' + name);
  });
}
