import React from 'react'

function cityLayout({children, info}) {
  return (
    <div className='flex'>
      {children}
      {info}
    </div>
  )
}

export default cityLayout