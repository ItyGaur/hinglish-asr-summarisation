# Video (screen-text) judging packets

Judge: the SAME judge as the paper (Claude Sonnet 5.5, chat). Start a NEW chat, paste the instructions block once, then paste one window block at a time and copy the reply lines into judge_video_responses.txt. If the chat gets long (about 8 windows), start a new chat and paste the instructions block again.

## Instructions block (paste first)

```
You are a strict, consistent evaluator of summary content.

Decide, for each numbered fact, whether the SUMMARY conveys it.

A fact is supported if the summary states its core information or clearly implies it, even in different words, in another language (English, Hindi or Hinglish) or in another script. It is not supported if it is missing, only vaguely related, or contradicted. Judge each fact independently, using only the summary.

Additional rules (apply identically to every summary):
1. Facts whose core is a specific path, shortcut, value or name (e.g. "File > Save", "Ctrl+Alt+T", "228") need that specific element; a generic mention does not count.
2. A contradicted fact (wrong value/direction) is unsupported.
3. A garbled product name does not by itself cancel a correctly stated fact.
4. Hallucinated content never supports a fact.

For each SUMMARY id I send, reply with exactly one line: <id>: <bit string>, one digit per fact in order (1 = supported, 0 = not supported). No other text.
```

## Window W01  (10 facts, 7 summaries)

```
FACTS:
1. A slide background refers to all colors and effects applied behind the content of the slide.
2. Any alteration made to the master slide applies to every slide in the presentation.
3. The Slide Master view is opened by navigating to View, selecting Master, and clicking Slide Master from the main menu.
4. The master view toolbar can be used to create, delete, and rename master pages.
5. A white background can be applied by choosing the blank option under bitmap fill in the Page Setup dialog box.
6. The text color can be set to black from the Font Effects tab within the Character dialog box.
7. A light blue color can be applied to a slide by selecting Blue 8 from the color fill dropdown menu in Page Setup.
8. The basic shapes toolbar at the bottom of the screen allows users to draw various basic shapes.
9. When drawing a rectangle, the cursor displays a plus sign accompanied by a capital letter I.
10. The control points that appear on a selected object are eight small blue squares used to resize it.

SUMMARY VD-W01-a:
<<<
This tutorial covers the use of LibreOffice Impress, focusing on creating and customizing slide backgrounds and designs. It explains how to apply various background options and create custom backgrounds. The tutorial also demonstrates how to edit the title and outline text formats, change case, and adjust paragraph settings. Additionally, it shows how to manipulate slide layouts, insert charts, and manage master pages. The video guides users through the interface, including the task pane, slide sorter view, and various formatting tools. Overall, the tutorial aims to help users create visually appealing and effective presentations using LibreOffice Impress.
>>>

SUMMARY VD-W01-b:
<<<
This tutorial explains how to apply backgrounds and designs to slides using LibreOffice Impress on a GNU/Linux operating system. It covers customizing slide masters and applying them across all slides. To change the background, you select the Slide Master, then choose the desired background from the Format menu. For a white background, you set the fill to bitmap and choose blank. Changing text color to black improves readability against a white background. Adding colors or shapes involves selecting the appropriate options from the context menu or toolbar. The tutorial also demonstrates adding elements like logos and shapes, such as rectangles, to slides. Overall, it guides users through creating visually appealing presentations with customized backgrounds and designs.
>>>

SUMMARY VD-W01-c:
<<<
The tutorial explains how to customize slide backgrounds and designs in LibreOffice Impress using a Linux operating system. It covers creating and applying custom backgrounds, adjusting text colors, and modifying shapes within slides. To create a custom background, users select the "Slide Master" option from the "View" menu, then choose the desired background style such as bitmap or solid color. Users can also change text formatting and add shapes like rectangles to slides. The tutorial demonstrates how to adjust the size and position of these elements, ensuring they fit well with the chosen background. Additionally, it shows how to apply these changes consistently across all slides in a presentation.
>>>

SUMMARY VD-W01-d:
<<<
This tutorial explains how to customize backgrounds and designs in LibreOffice Impress, using a Linux operating system and version 334 of the LibreOffice suite. The tutorial covers creating custom backgrounds and applying them to slides. To start, open the sample presentation "sampleimpress odp" and select the "Slide Master" option from the menu. This allows changes made to the master slide to apply to all slides in the presentation. 

To create a custom background, choose the "Page Background" option from the "Format" menu. Select "Bitmap" and then "Blank" to remove any existing background. Adjust text color to ensure it contrasts well with the new background. For example, change the text color to black if the background is white. 

The tutorial also demonstrates adding shapes and logos to slides. Use the "Basic Shapes" toolbar to draw shapes like rectangles and circles. Place these shapes over the slide content and adjust their size and position using the handles around the shape. This process helps in designing visually appealing presentations with consistent backgrounds and elements.
>>>

SUMMARY VD-W01-e:
<<<
This tutorial covers creating and customizing slide masters and designs in LibreOffice Impress. It starts with setting up the background for all slides using the Slide Master. Users learn to access and modify the Slide Master by clicking on the 'Master' and then 'Slide Master' options from the menu. They can also customize the background color and text formatting for all slides uniformly. The tutorial demonstrates changing the background to white and adjusting text color for better visibility. It further explains how to add shapes like rectangles, circles, and triangles to slides using the Basic Shapes toolbar. Users can create and position these shapes on the slide by clicking and dragging. The tutorial also shows how to align the edges of shapes precisely using control points. Overall, it provides a comprehensive guide to designing consistent and visually appealing presentations in LibreOffice Impress.
>>>

SUMMARY VD-W01-f:
<<<
This tutorial explains how to customize slide backgrounds and designs using LibreOffice Impress on GNU Linux. It covers setting up custom backgrounds for all slides through the slide master. To do this, you first open a sample presentation and select the Slide Master view from the main menu. Here, you can modify the master slide, which changes for all slides in the presentation. You can also add custom backgrounds by selecting the Backgrounds tab and choosing options like Bitmap or Blank. For text clarity, choose a contrasting color. To add design elements, use the Basic Shapes toolbar to insert shapes like rectangles or circles. Position these shapes over the title area and adjust their size and shape using the control handles. This tutorial demonstrates creating a custom background and adding shapes to enhance your presentation's visual appeal.
>>>

SUMMARY VD-W01-g:
<<<
The tutorial covers how to use LibreOffice Impress to customize slide backgrounds and designs. It starts with creating a custom background for slides using the Slide Master feature. Users can apply various background options and effects to the entire slide, including setting a custom background color or pattern. The tutorial explains how to access the Slide Master view from the menu, where users can modify the background and other design elements consistently across all slides.

To add shapes to slides, the tutorial demonstrates using the Basic Shapes toolbar to draw rectangles, circles, and other shapes. Users can then manipulate these shapes by dragging their handles and adjusting control points to align them precisely.

The tutorial also covers formatting text within slides. Users can change text styles, colors, and alignment using the Text Edit tool. They learn how to apply different fonts, sizes, and effects to text, ensuring it stands out against the background.

Additionally, the tutorial shows how to insert and format tables, charts, and other objects on slides. It explains how to position and size these elements relative to the slide layout, and how to customize their appearance using various fill and border options.

Overall, the tutorial provides step-by-step guidance on enhancing the visual appeal and organization of presentations in LibreOffice Impress.
>>>
```

## Window W09  (11 facts, 7 summaries)

```
FACTS:
1. The Impress workspace has five tabs known as view buttons.
2. Notes view enables users to attach notes to each slide that do not show up during the presentation.
3. Handout view provides the capability to print slides as handouts and select how many slides appear per page.
4. The Slides pane on the left of the screen shows thumbnails of the presentation slides.
5. A new blank slide can be added after a selected slide by choosing Insert and then Slide.
6. A duplicate slide can be created by clicking Insert and then Duplicate Slide.
7. In Slide Sorter view, a slide can be copied and pasted after the final slide by selecting the After option.
8. Font family and font size can be adjusted using the text format toolbar.
9. A dialog box to customize font style and size can be opened by selecting Character under the Format menu.
10. Font color can be altered by clicking the down arrow situated next to the font color icon.
11. Text formatting options such as bold, italics, and underline can be applied using toolbar icons.

SUMMARY VD-W09-a:
<<<
This tutorial from the Spoken Tutorial project covers how to use LibreOffice Impress to create presentations. It begins with an overview of the Impress window, including its various menus and tools such as File, Edit, View, Insert, Format, Tools, and Slide Show. The tutorial explains how to insert slides, format fonts, and customize animations. It also discusses the benefits of open-source software and outlines a short-term strategy for creating effective presentations. The presentation includes slides on long-term goals, potential alternatives, and development plans. Throughout, the tutorial emphasizes the use of various features like charts, tables, and multimedia elements to enhance the presentation.
>>>

SUMMARY VD-W09-b:
<<<
This tutorial covers creating and formatting presentations using LibreOffice Impress on GNU/Linux. It explains how to navigate the Impress interface, including the various view options like Normal, Outline, Notes, Handout, and Shorter views. Key features include inserting new slides by selecting another slide, right-clicking, and choosing Duplicate Slide or Copy-Paste. The tutorial also demonstrates changing fonts and formatting text. For example, it shows how to change the font type from Albany to Aerial Black and adjust the font size from 23 to 40. Additionally, it explains how to change text color and apply formatting such as bold, italic, and underline to specific lines of text within slides.
>>>

SUMMARY VD-W09-c:
<<<
The tutorial covers how to create and format presentations using LibreOffice Impress. It starts with explaining the different parts of the Impress window, such as the slide insertion, formatting options, and various tabs like Normal, Outline, Notes, and Handout. The speaker demonstrates how to insert new slides, copy existing ones, and organize them in the Slide Sorter view. 

Key points include:
- Using the Insert menu to add slides
- Formatting text and fonts 
- Changing slide layouts and designs
- Adding titles and text to slides
- Customizing animations and transitions between slides
- Saving and printing the presentation

The tutorial uses a sample presentation file named "Sample Impress.odp" to demonstrate these features. The speaker explains step-by-step how to perform common tasks like inserting slides, formatting text, and customizing the appearance of slides for a professional-looking presentation.
>>>

SUMMARY VD-W09-d:
<<<
This tutorial covers how to create and format a presentation in LibreOffice Impress, using Ubuntu Linux 10.04 as the operating system. Key features include:

1. Understanding the Impress window layout, including tabs like Normal, Outline, Notes, Handout, and Slide Sorter views.
2. Inserting new slides by selecting another slide, clicking Insert > Duplicate Slide, or right-clicking a slide and choosing Copy/Paste.
3. Formatting text by selecting text, changing font style and size, and applying bold, italic, and underline effects.
4. Copying slides by right-clicking a slide and choosing Copy, then pasting it elsewhere.
5. Changing text color and font by selecting text, clicking the Font Color icon, and choosing from available colors.

The tutorial demonstrates these steps using sample presentations and provides a comprehensive guide for creating and editing presentations in LibreOffice Impress.
>>>

SUMMARY VD-W09-e:
<<<
The tutorial covers creating and formatting slides in LibreOffice Impress, using Linux and LibreOffice version 3.3.4. It explains how to insert slides, customize layouts, and add text. Key steps include selecting the Normal tab, inserting a new slide, and adding a title by clicking on the Text Box. The tutorial demonstrates how to copy and paste slides, edit text size and style, change fonts, and apply custom colors. It also shows how to use the Font dialog box to set font styles and colors, and how to format text as bold, italic, or underlined.
>>>

SUMMARY VD-W09-f:
<<<
This tutorial covers how to create and format presentations using LibreOffice Impress on GNU/Linux with version 334. It explains the different views available in Impress, such as Normal, Outline, Notes, Handout, and Slide Sorter. Key features include inserting and duplicating slides, formatting fonts, and copying slides. To insert a new slide, select another slide, then click Insert > Slide. To duplicate a slide, click Insert > Duplicate Slide or right-click a slide, choose Copy, navigate to the desired location, and paste. For font formatting, double-click a slide, select the text box, and change the font style and size through the Text Formatting toolbar or the Format > Character dialog box. To change text color, select the text, click the Font Color icon, and choose a color from the dropdown menu. Bold, italic, and underline can also be applied using their respective icons.
>>>

SUMMARY VD-W09-g:
<<<
This tutorial covers how to create and format a presentation in LibreOffice Impress, using Ubuntu Linux 10.04 as the operating system. Key features of the Impress window include the view buttons (normal, outline, notes, handout, and slide sorter), the slides pane, and the tasks pane with layout options. The tutorial explains how to insert and copy slides, and demonstrates formatting text by changing fonts, sizes, colors, and applying bold, italic, and underline styles. It also shows how to use the context menu for copying and pasting slides, and how to modify the appearance of text within slides.
>>>
```

## Window W21  (10 facts, 7 summaries)

```
FACTS:
1. A presentation can be printed by selecting File then Print or by pressing the Ctrl and P keys together.
2. Under the Document field in the General tab, available presentation print options include slides, handouts, notes, and outline.
3. In the LibreOffice Impress tab under Content, users can choose to print the slide name, date and time, and hidden pages.
4. Selecting the draw a border around each page option creates a black border around each printed page.
5. The brochure option formats slides to be printed as a booklet suitable for binding.
6. The default handout configuration places four slides per page ordered from left to right and then down.
7. Size options under the LibreOffice Impress tab are disabled when printing handouts because print size is determined by sheet size and slide count.
8. Notes for a slide can be added by navigating to the slide and clicking the Notes tab.
9. Selecting notes under the Document field displays typed slide notes at the bottom of the slide in the print preview.
10. Size options in the LibreOffice Impress tab are unavailable when printing notes.

SUMMARY VD-W21-a:
<<<
This tutorial explains how to print presentations in LibreOffice Impress, using GNU/Linux as the operating system and version 3.3.4 of LibreOffice. To print slides, you can open your presentation, then go to File > Print or use Ctrl+P. In the General and Options tabs, you can choose specific options for printing slides, such as including slide names, dates, and hidden pages in grayscale or color. You can also select how many slides to print per page and customize the layout. For handouts, choose Handout from the Document field in the Print section, which defaults to four slides per page. Notes can be printed by selecting Notes from the Document field in the Print section, though fewer customization options are available. Finally, clicking the Print button will start the printing process if the printer is correctly configured.
>>>

SUMMARY VD-W21-b:
<<<
The tutorial explains how to print presentations using LibreOffice on a Linux system with version 3.3.4. It covers various printing options available in LibreOffice Impress. To print slides, you first select the desired slides from the sample presentation, set the print settings such as color, page range, and slide layout, and choose which parts of the slides to print. For single-page printing, you can select specific slides and use the "Handouts" option to print multiple slides per page. The tutorial also demonstrates how to print notes by typing them into the notes section and then printing them along with the slides. Additionally, it shows how to upload and print documents directly from the LibreOffice Impress tab. Overall, the tutorial provides a comprehensive guide on utilizing the printing features in LibreOffice for creating and distributing presentations.
>>>

SUMMARY VD-W21-c:
<<<
In this tutorial, you learn how to print presentations in LibreOffice Impress using various options. You can print slides, handouts, and notes. The tutorial uses Ubuntu Linux 10.04 and LibreOffice 3.3. To print slides, go to File > Print and select the desired options like color, grayscale, or black and white. For handouts, choose the number of slides per page and arrange them accordingly. Notes can be printed by selecting the Notes tab and then printing. The tutorial covers settings in the General and Options tabs, such as document fields, page layout, and print preview. It also discusses arranging slides on multiple sheets and creating borders around each page for better presentation.
>>>

SUMMARY VD-W21-d:
<<<
This tutorial covers how to print presentations in LibreOffice Impress, using GNU Linux as the operating system. It explains various print options available for slides, handouts, outlines, and notes. To print slides, you can select them from the General tab under the Print dialog. You can choose to print slides, handouts, outlines, or notes in specific formats like grayscale or fit to page. For handouts, you can choose the number of slides per page and arrange them accordingly. Notes can be printed by selecting the Notes tab and choosing the appropriate print option. The tutorial also mentions adjusting the print size based on the number of slides per page and ensuring the printer is correctly configured before printing.
>>>

SUMMARY VD-W21-e:
<<<
In this tutorial, you learn how to print presentations in LibreOffice Impress using Ubuntu Linux 10.04 and LibreOffice 3.3. The tutorial covers printing slides, handouts, and notes. To print slides, select the desired slides and choose the appropriate settings under the "General" and "Options" tabs. For handouts, you can specify the number of slides per page and the order. Notes can be printed by selecting the "Notes" option in the print dialog. The tutorial also explains how to configure the printer and set the document size. Additionally, it demonstrates how to create a print job for collated output and print in reverse page order. The presentation includes examples of how to customize the print layout and settings for different types of documents.
>>>

SUMMARY VD-W21-f:
<<<
This tutorial covers how to print presentations in LibreOffice Impress on Ubuntu Linux 10.04. It explains three printing options: slides, handouts, and notes. The tutorial demonstrates navigating the Impress interface, including the menu bar and document layout. Key steps include selecting the desired print option, configuring settings such as number of copies and page layout, and choosing between color and black & white prints. The tutorial also highlights benefits of open-source software like reducing vendor dependence and increasing accessibility.
>>>

SUMMARY VD-W21-g:
<<<
In this tutorial, you learn how to print presentations in LibreOffice Impress using various options such as slides, handouts, notes, and outlines. The tutorial uses Ubuntu Linux 10.04 and LibreOffice 3.3. To print slides, go to `File > Print` or use `Ctrl + P`. You can choose to print slides in their original colors, grayscale, or black and white. For handouts, select `Handouts` in the `Document` field under `Print`. Notes can be printed by selecting `Notes` in the `Document` field. The tutorial covers settings like slides per page, page layout, and options for borders and layouts. It also discusses how to configure the printer and ensure correct settings for printing.
>>>
```

## Window W23  (11 facts, 7 summaries)

```
FACTS:
1. LibreOffice Impress opens in Normal view by default.
2. Users can return to Normal view by clicking the Normal tab or selecting View and then Normal.
3. Slides can be created and edited in Normal view.
4. Slide designs can be selected and changed from the Master Pages section of the Tasks pane.
5. Outline view arranges slide contents sequentially below one another like a table.
6. Outline view allows rearranging line items by moving them up, down, or across lines.
7. Slide Sorter view is used to sort slides into any desired sequence.
8. Notes view allows presenters to write speaker notes to assist them during a presentation.
9. Notes written in Notes view remain visible to the presenter on the monitor but hidden from the audience.
10. The Tasks pane can be displayed or hidden by clicking View and selecting Tasks Pane.
11. The slide layout can be changed using the Layout section in the Tasks pane.

SUMMARY VD-W23-a:
<<<
This tutorial covers various view options in LibreOffice Impress, a presentation software. It starts with the default Normal view and explains how to switch between different views like Outline, Slide Sorter, and Notes. The tutorial demonstrates changing slide designs using the Master Pages feature, which can be accessed from the Tasks Pane. Users learn to rearrange slides, modify slide layouts, and adjust the presentation layout. Key features discussed include the Outline view for organizing slides, Slide Sorter for reordering slides, and Notes view for adding notes that appear on the presenter's screen but not the audience's. The tutorial also shows how to customize the background and title areas of slides using Master Pages. Overall, it guides users through creating a new presentation with a dark blue background and light blue title area, encouraging them to practice these skills.
>>>

SUMMARY VD-W23-b:
<<<
The tutorial covers various view options in LibreOffice Impress, a presentation software. It starts with the default Normal view and explains how to switch between different views like Outline, Notes, and Slide Sorter. Key points include:

- Using the Normal view to design slides and edit them.
- Switching to Outline view to organize slide contents hierarchically.
- Adjusting slide layouts using the Layouts section.
- Adding notes for the presenter's reference in Notes view.
- Rearranging slides in Slide Sorter view.
- Customizing the presentation layout using Master Pages.

The tutorial demonstrates these features using a sample presentation titled "Sample-impress.odp" and provides guidance on creating a new presentation with a dark blue background and light blue title area. It also mentions the importance of Open Source software and its benefits.
>>>

SUMMARY VD-W23-c:
<<<
This tutorial from the Spoken Tutorial project explains how to use LibreOffice Impress on Ubuntu Linux 10.04. It covers navigating the software interface, including menus like File, Edit, View, Insert, Format, Tools, and Slide Show. Key features discussed include layouts, slides, and the slide sorter view. The tutorial emphasizes the benefits of open-source software, such as reducing costs and dependency on specific vendors. It also highlights the importance of planning and long-term strategies for successful presentations. The final slides suggest using notes during the presentation so the speaker can see them while the audience does not. Overall, the tutorial provides an overview of using LibreOffice Impress for creating and presenting slideshows.
>>>

SUMMARY VD-W23-d:
<<<
The tutorial covers the features and usage of LibreOffice Impress for creating presentations in the Linux environment. It explains how to switch between normal and slide view, create and edit slides, and add content such as tables and bullet points. Users can also customize slide layouts and notes, which can be accessed during the presentation. The tutorial demonstrates how to use the task pane to upload slides, navigate through slides, and apply various formatting options like background colors. Additionally, it shows how to use the notes page to take notes during the presentation and how to adjust the slide sorter view for better organization. Overall, the session aims to help users create professional-looking presentations with a dark background and light text, using the features of LibreOffice Impress effectively.
>>>

SUMMARY VD-W23-e:
<<<
The tutorial covers how to use LibreOffice Impress for creating and presenting slides. It explains the different views available such as Normal, Outline, Notes, and Slide Sorter. The Normal view shows the complete slide layout, while the Outline view organizes slides with bullet points for easy editing. Users can change slide designs using the Master Pages feature. The Notes view allows adding notes for the presenter's reference during the presentation. The tutorial also demonstrates how to rearrange slides and customize the presentation layout. Key concepts include using the Task Pane for layout changes and understanding the benefits of Open Source software in creating presentations. The sample presentation uses a dark blue background and light blue title areas, showcasing how to apply these settings.
>>>

SUMMARY VD-W23-f:
<<<
The tutorial covers how to use LibreOffice Impress for creating and presenting slides. It explains the different view modes such as Normal, Outline, Notes, and Slide Sorter. The Normal view allows you to work on slides while the Outline view shows the structure of the presentation. Notes can be added to help remember what to say during the presentation. The Slide Sorter view helps organize slides before the presentation. The tutorial also discusses how to customize the appearance of slides, including layout options and color schemes. It emphasizes the benefits of using Open Source software like LibreOffice, which includes reducing costs and dependency on proprietary software. The presentation concludes with tips on how to effectively use notes during a presentation and thanks the presenter.
>>>

SUMMARY VD-W23-g:
<<<
This tutorial covers how to use various view options in LibreOffice Impress, a presentation software. It starts with the default Normal View, where you can see and edit slides. Other views include Slide Sorter for organizing slides in a specific order and Outline View for seeing the structure of your presentation as a hierarchical list. You can change slide designs using the Master Page section, which allows you to modify the overall look of your presentation. Notes View lets you write notes that will appear on your screen but not for the audience. The tutorial also explains how to rearrange slides by dragging them to new positions. Additionally, it demonstrates changing the layout of slides and adjusting the presentation layout through the Task Pane. The key takeaway is understanding how to effectively use these features to create and customize presentations in LibreOffice Impress.
>>>
```
