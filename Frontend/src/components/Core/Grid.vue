<template>
  <section class="py-10">
    <div class="grid grid-cols-3 gap-4 items-stretch">
      <!-- Left Side - Large Illustration Box -->
      <div class="col-span-2 bg-lightblue p-4 rounded-xl flex flex-col items-center text-center">
        <img src="/src/assets/img/illustration.png" alt="Illustration" class="w-1/2 h-auto mb-4"> 
        <div class="max-w-md">
          <h3 class="font-bold text-lg">Can’t find job options and opportunities</h3>
          <p class="text-gray-700 mt-2 text-sm">
            Use clear frameworks that will help you find the right field and land opportunities.
          </p>
        </div>
      </div>

      <!-- Right Side - Two Stacked Sections -->
      <div class="col-span-1 flex flex-col gap-4">
        <!-- Top Box -->
        <div class="bg-lightblue p-4 rounded-xl flex flex-col items-center text-center h-1/2">
          <img src="/src/assets/img/illustration2.png" alt="Career Exploration" class="w-32 h-32 mb-2"> 
          <h3 class="font-bold text-sm">Not sure what you want to do</h3>
          <p class="text-gray-700 mt-2 text-xs">
            Get step-by-step guides to explore and identify career options which you like.
          </p>
        </div>

        <!-- Bottom Row (Side-by-Side) -->
        <div class="grid grid-cols-2 gap-4 h-1/2">
          <!-- Small Square Box -->
          <div class="bg-white p-3 rounded-xl shadow border flex flex-col items-center justify-center">
            <span class="text-3xl">😩</span>
            <h3 class="font-bold text-sm text-center mt-2">Stressed about your future!</h3>
          </div>
          <!-- Rectangular Box -->
          <div class="bg-lightblue p-3 rounded-xl flex items-center">
            <h3 class="font-bold text-sm text-left">
              Hate what you’re doing and don’t know how to make a career or job shift
            </h3>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
