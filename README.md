# Volunteering Opportunities Platform
#### Video Demo: https://youtu.be/nBLBFypnsnU
#### Description:

**Project Overview**
Many organisations in Singapore struggle to attract volunteers for their tutoring programmes. At the same time, students have difficulty finding opportunities that fit them. For instance, the location may be too far from their house. By creating this website, I hope to create a platform that solves both problems simultaneously. Organisations can set up accounts to post opportunities while volunteers can view the different options before registering for an opportunity that best fits them.

If I had more time or if I were working with groupmates, I would add a chat function to the website so that volunteers can contact organisations if they have more questions. I should at least add a line of the organisation's contact information too.

Another idea I had in mind was to add an accordion of FAQs. This answers the volunteer's questions more in-depth so they are more likely to sign up.

Furthermore, I realised that upon posting the opportunity, the organisation is unable to edit the text. Allowing them to do so would be better, since it prevents users from seeing low-quality posts.

I would also spend time optimising the input in the "post" tab. Currently, "math" is recognised as a different subject to "mathematics" so writing a programme to equate both (and other possibilities) would be crucial. I would also standardise the styles of the inputs. For instance, if someone did not capitalise the location, the computer still accepts the word. This leads to inconsistent display in the homepage. A better way would be to automatically capitalise the first letter of each word for instance.

**Topbar Navigation**
I wanted a simple navigation page so I kept the number of headings to just 3. The register page would be under the login page.

**Register**
For the register page, I required an email, username and password. I asked for the user's email as it would allow me to send promotional emails to the user in the future.

**Home**
The home page is also the index page, where all the volunteering opportunities are displayed. I coded it such that the title of each opening is the location. I also included other important information such as the subjects, levels, etc.

I used a card layout as I had many "clusters" of information and it would look neater than a table. I struggled with getting the card grids in Bootstrap to work, so there is only one card per row.

When one pressed "register", I opened a confirmation pop-up (using the Bootstrap modal component) for the user to confirm that they are signing up for the volunteering opening. This is to prevent users from accidentally signing up for the opening.

**Post**
Any user can also post a volunteer tutoring opportunity that they know. Upon entering the details, they would be uploaded into the database, which would be shown to all users on their homepage. Each opening also includes the username of the user who posted that opportunity.

Upon successfully adding a post, "Successfully added!" would appear in green below the inputs. I considered adding a dialogue box but I thought that it would be unnecessarily distracing.

**History**
Whenever a user signs up for a volunteering opportunity, it would record the details into a database, and display the sign up details in the "History" tab. This is to remind the user of the openings that they signed up for. It also includes the date and time of when the user signed up.

I decided to display the data in a table as that's the easiest way to see the sign up details. Cards wouldn't work as the user isn't choosing between different options, they were merely viewing the history of their sign ups.

To display the history, I was debating between creating a new table and using the same table where the index was drawn. I decided to create a new table as there were some disparities between the data displayed so I wanted a clearer distinction.
