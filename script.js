const mediaFolder = "media"; 
const galleryContainer = document.getElementById('gallery-container');

fetch(`${mediaFolder}/media_list.json`)
  .then(response => response.json())
  .then(data => {
    data.forEach(item => {
      const galleryItem = document.createElement('div');
      galleryItem.classList.add('gallery-item');
      galleryItem.style.width = '210px'; 
      galleryItem.style.height = '150px'; // Title height (50px) + Image Height (100px) 

      const mediaElement = document.createElement(item.url.endsWith('.gif') ? 'img' : 'video');
      mediaElement.src = `${mediaFolder}/${item.url}`;
      mediaElement.alt = item.title; 
      mediaElement.style.width = '210px';
      mediaElement.style.height = '100px';
      mediaElement.style.objectFit = 'cover'; // For cropping

      const titleOverlay = document.createElement('div');
      titleOverlay.classList.add('title-overlay');
      titleOverlay.textContent = item.title;

      galleryItem.appendChild(mediaElement);
      galleryItem.appendChild(titleOverlay);

      galleryContainer.appendChild(galleryItem);
    });
  })
  .catch(error => console.error("Error fetching media:", error)); 
