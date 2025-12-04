"use client"

import { useParams } from 'next/navigation'
import React from 'react'

function Page() {
  const {city} = useParams()
  return (
    <div className='text-white mt-25 w-[50%]'>{city} is a beautiful city</div>
  )
}

export default Page