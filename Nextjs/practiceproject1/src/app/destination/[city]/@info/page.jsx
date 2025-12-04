"use client"

import { useParams } from 'next/navigation'
import React from 'react'

function Page() {
  const {city} = useParams()
  return (
    <div className='mt-25 w-[50%]'>
      {city} is the  best city
    </div>
  )
}

export default Page