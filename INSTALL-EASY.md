# Install AI Boardroom (Non-Technical Guide)

A step-by-step walkthrough for anyone who has never touched GitHub before. No coding, no terminal, no GitHub account required.

If a friend, client, or executive asks "how do I use this thing?" send them here.

---

## What You Need First

1. **Claude Desktop app** installed on your computer
   - Download free at: [claude.ai/download](https://claude.ai/download)
   - Available for Mac and Windows
2. **A Claude account** (free tier works to start, Pro recommended for heavy use)
3. **About 5 minutes**

That's it.

---

## Step 1: Go to the GitHub Page

1. Open your web browser
2. Go to: [github.com/evoputa/ai-advisory-board](https://github.com/evoputa/ai-advisory-board)
3. You will see a page with a description, a file list, and a green button that says **"Code"**

Don't be intimidated by the file list. You only need one thing from this page.

---

## Step 2: Download the Skill

1. Click the green **"Code"** button (top right of the file list)
2. A small menu appears
3. Click **"Download ZIP"**
4. A file called `ai-advisory-board-main.zip` downloads to your computer

---

## Step 3: Unzip the File

**On Windows:**
1. Find the downloaded ZIP in your Downloads folder
2. Right-click it
3. Choose **"Extract All"**
4. Click **"Extract"**
5. You now have a folder called `ai-advisory-board-main`

**On Mac:**
1. Find the downloaded ZIP in Downloads
2. Double-click it
3. It automatically unzips into a folder

---

## Step 4: Rename the Folder

1. Find the unzipped folder (`ai-advisory-board-main`)
2. Rename it to just **`ai-advisory-board`** (remove the "-main" part)
   - Windows: right-click, Rename
   - Mac: click once, press Enter, type new name

This rename matters. Claude looks for the exact folder name.

---

## Step 5: Move the Folder Into Claude's Skills Location

Claude Desktop has a special folder where it looks for skills. You need to put the AI Boardroom folder there.

**On Windows:**
1. Open File Explorer
2. In the address bar at the top, paste this exactly: `%USERPROFILE%\.claude\skills`
3. Press Enter
4. If the folder doesn't exist, create it: go to `%USERPROFILE%\.claude\` and make a new folder called `skills`
5. Drag your `ai-advisory-board` folder INTO the `skills` folder

**On Mac:**
1. Open Finder
2. Press `Cmd + Shift + G`
3. Paste: `~/.claude/skills`
4. Press Enter
5. If the folder doesn't exist, create it
6. Drag your `ai-advisory-board` folder INTO the `skills` folder

---

## Step 6: Restart Claude Desktop

1. Quit Claude Desktop completely (not just close the window)
   - Windows: right-click the Claude icon in the system tray, choose Quit
   - Mac: Claude menu, Quit Claude
2. Open Claude Desktop again

---

## Step 7: Test It

1. Open a new chat in Claude Desktop
2. Type this exact message:

   > Use the ai-advisory-board skill. I'm thinking about raising prices on my consulting services by 30%. Convene the right advisors and tell me what they think.

3. Hit Enter

Claude will load the skill, pick the right advisors from the 109 leaders, and give you a full board session with multiple perspectives, disagreements, and a recommendation.

---

## What to Ask Your Boardroom

Good questions to get started:

- "Should I hire a VP of Sales or stay founder-led for another year?"
- "I'm deciding between two pricing models. Convene the board."
- "We're losing customers to a cheaper competitor. What would the board do?"
- "Should I take this $500k investor offer or bootstrap longer?"
- "I want to launch in a new market. Pressure-test this for me."

The board works best when you give it:
1. **Context** (what's going on)
2. **The decision** (what you're trying to figure out)
3. **Constraints** (budget, time, team size)

---

## Getting Updates

**Important:** The ZIP method is a one-time snapshot. You will not automatically get new advisors, improved prompts, or fixes.

To update:
1. Come back to [github.com/evoputa/ai-advisory-board](https://github.com/evoputa/ai-advisory-board)
2. Download the ZIP again
3. Replace your existing `ai-advisory-board` folder with the new one
4. Restart Claude Desktop

A good rhythm is once a month.

---

## Troubleshooting

**"Claude says it can't find the skill"**
- Check the folder is named exactly `ai-advisory-board` (no "-main")
- Check it's in `~/.claude/skills/` (Mac) or `%USERPROFILE%\.claude\skills\` (Windows)
- Make sure you fully quit and reopened Claude Desktop

**"The skills folder doesn't exist"**
- That's normal. Just create it manually inside the `.claude` folder.

**"I can't see the .claude folder"**
- It's hidden by default
- Mac: in Finder press `Cmd + Shift + .` to show hidden files
- Windows: in File Explorer, View menu, check "Hidden items"

**"Claude isn't using the skill even though I asked"**
- Be more explicit: start your message with "Use the ai-advisory-board skill to..."

---

## What You Don't Need to Worry About

- You do NOT need a GitHub account
- You do NOT need to know how to code
- You do NOT need to use the terminal or command line
- You do NOT need to "install" anything in the technical sense
- The skill runs entirely on your computer through Claude Desktop

If you can download a ZIP and drag a folder, you can use AI Boardroom.
