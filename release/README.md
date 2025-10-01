# Instagram Followers Analyzer

A Windows desktop application that analyzes your Instagram followers and following data to identify who is not following you back.

## 🚀 How to Use

### Step 1: Get Your Instagram Data

1. Go to Instagram Settings → Privacy and Security → Data Download
2. Request your all-time followers data download (choose JSON format)
3. Wait for Instagram to prepare your data (usually takes a few minutes depending on your profile data size)
4. Download and extract the files

### Step 2: Locate Required Files

From your Instagram data download, you need:

- `followers_1.json` (or similar) - Contains your followers list
- `following.json` - Contains your following list

### Step 3: Run the Application

1. Double-click `Instagram_Followers_Analyzer.exe`
2. Click "Browse" next to "Followers JSON" and select your followers file
3. Click "Browse" next to "Following JSON" and select your following file
4. Click "Analyze Followers" to start the analysis

### Step 4: View Results

The application will show:

- Total number of people you're following
- Total number of your followers
- Your follow ratio (followers/following)
- Complete list of users who don't follow you back

## 📊 Features

- **User-Friendly Interface**: Clean, intuitive GUI
- **File Browser**: Easy file selection with browse dialogs
- **Progress Tracking**: Real-time status updates and progress bar
- **Detailed Results**: Comprehensive analysis with statistics
- **Error Handling**: Clear error messages for troubleshooting
- **No Installation Required**: Standalone executable

## 🔒 Privacy & Security

- **100% Local Processing**: All analysis happens on your computer
- **No Data Upload**: Your Instagram data never leaves your device
- **No Internet Required**: Works completely offline
- **No Data Storage**: The app doesn't save or store your data

## 📝 File Information

- **Instagram_Followers_Analyzer.exe**: The main application (standalone)
- **README.md**: This documentation file

## ⚠️ Important Notes

- Make sure your JSON files are from Instagram's official data download
- The app supports Instagram's standard JSON format
- Large follower lists may take a few seconds to process
- The application requires Windows 7 or later

## 🐛 Troubleshooting

**"Error during analysis" message:**

- Verify you selected the correct JSON files
- Ensure the files are not corrupted
- Check that the files follow Instagram's JSON format

**Application won't start:**

- Make sure you're running on a supported Windows version
- Try running as administrator if needed
- Check that the executable isn't blocked by antivirus software

**No results showing:**

- Verify both files are selected before clicking "Analyze Followers"
- Check that your JSON files contain the expected data structure

## 💡 Tips

- The app will show "Everyone you follow is following you back!" if no unfollowers are found
- Results are numbered for easy reference
- You can scroll through large lists in the results area
- The status bar shows current operation progress

---

**Version**: 1.0  
**Platform**: Windows  
**License**: Free for personal use
